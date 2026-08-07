# Suno: персона и дрейф голоса

## Проблема дрейфа
После ~2-го куплета (около 1.5 минут) вокал начинает отходить от persona-референса и становится больше «суновским», чем персонализированным. Чем дальше — тем сильнее.

## Причины
- Suno постепенно «забывает» референс по ходу длинной генерации
- Persona-якорь слабеет на расстоянии от начала

## Обходные (в процессе проверки)
- Держать треки короче — разбивать на части и экстендить
- Использовать extensions от сильного участка а не от конца
- Регенерировать с того же persona когда дрейф заметен

[источник: TG suno_promt_rus, henry_morgann (вопрос), 2026-06-13]

---

## Persona Creation Flow (API, 6 шагов)

> Source: paperfoot/suno-cli API_INTELLIGENCE.md, captured April 2026
> Нужен: JWT auth, S3 upload, ~2 аудиофайла (sample + verification)

### Шаг 1: Загрузка voice sample
S3 presigned upload → `POST /api/uploads/audio/{upload_id}/upload-finish/`
Response: `200 OK` (empty body)

### Шаг 2: Poll upload status
`GET /api/uploads/audio/{upload_id}/`
Response: JSON со статусом обработки.

### Шаг 3: Extract vocal stem
`POST /api/processed_clip/voice-vox-stem`
Body: `{"upload_id": "<id>"}`. Извлекает чистый вокал из загруженного аудио.

### Шаг 4: Запись verification phrase
Юзер читает: *"Listening to the melody of a gentle summer breeze"*
Второй upload через тот же flow с новым upload_id.

### Шаг 5: Voice verification
`POST /api/voice-verification/`
Body: оба upload_id + verification text. Проверяет что голос совпадает.

### Шаг 6: Create persona
`POST /api/persona/create/`
Payload ~47KB (вероятно base64 audio). Создаёт персону из проверенных клипов.

### Заметки
- Шаги 1-2 повторяются для каждого аудиофайла (sample + verification)
- S3 presigned URL генерируется до upload-finish (endpoint не захвачен)
- Verification phrase фиксированная — Suno проверяет именно её
- Через веб-интерфейс Suno этот flow автоматизирован в UI

[source: paperfoot/suno-cli API_INTELLIGENCE.md, 2026-07]

---

## Дрейф модели между версиями (смежный сигнал)

После релиза v5.5 (26.03.2026) часть пауэр-юзеров сообщает: старые треки при переоткрытии или ремастере звучат с другим вокалистом (r/SunoAI, FB-группа Suno Studio, весна 2026). Это НЕ persona-drift внутри одной генерации, а смена поведения самой модели между версиями. Практические следствия: правило пайплайна «одна версия Suno на EP» (release_v1, этап 5) покрывает это внутри релиза; при ремастере старого материала ожидать смену тембра и не считать это локальным багом генерации.

[источники: r/SunoAI «v5.5 ruined Suno» (май 2026), FB Suno Studio group (30.03.2026) — см. issue #41]
