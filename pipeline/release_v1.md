# Release Pipeline v1

Канон end-to-end: лирика → score → Suno-пакет → генерация → стем-микс → мастер → релиз → postmortem → правка KB.

[источник: Notion, 2026-07-11]

---

## Метрики прохода (жёсткие)

| Слой | Метрика | Порог |
|---|---|---|
| Лирика | Score (Детектор 2.0) | ≥ 7.0 (GOOD); цель EP ≥ 7.5 |
| Suno-пакет | Style + Lyrics tags + vocal anchor + negatives | все 4 блока заполнены |
| Генерация | 2–4 кандидата, выбран 1 | без визга / без пропадания ритм-секции в припеве |
| Микс | crest / peak (pre-master) | crest > 14 · peak < -3 dB |
| Мастер Spotify | LUFS / peak / crest | ≈ -14 LUFS · peak -1.5…-2.0 · crest 10–12 |
| Postmortem | 5 строк урока | записано в карточку + при необходимости в KB |

---

## Этапы (статусы = этапы базы)

### 1. Бриф
- Жанр/плейбук, BPM-диапазон, платформа, 1–2 референса саунда, ограничение вокала (baritone / no scream / whisper).
- Карточка в трекере: статус **Бриф**, поля Плейбук / BPM / Платформа / Заметки.

### 2. Черновик лирики
- Порядок энциклопедии §22.3: голос → якорь → форма → хук → черновик.
- Команды агента: `GENERATE` / `CALIBRATE` / `BLEND`.
- Черновик в Notion (черновики лирики) или в тело карточки трека.

### 3. Детектор
- Прогон через Детектор 2.0 (P1–P12, §25–28 v2.0 + white-list 25.27).
- `AUDIT` → `REPAIR` max 3 итерации.
- Записать Score лирики. Ниже 7.0 — не идти в Suno.

### 4. Suno-пакет
Взять готовый пакет плейбука (не импровизировать с нуля):
- `suno/packages/darksynth_coldwave.md`
- `suno/packages/folk_horror.md`
- `suno/packages/cloud_bedroom.md`

Минимум в карточке: Vocal anchor, Style-блок, behavior tags по секциям, negative constraints. Справка: `suno/` (промпты, версии, вокал-якоря).

### 5. Генерация
- 2–4 генерации, одна версия Suno на EP (не прыгать v3.5↔v5 без причины).
- Чек: плотность припева, регистр вокала, BPM-стабильность.
- Фикс плотности: `non-stop rhythm section, constant bass groove…`
- Фикс визга: процедура «рок без визга» (`suno/procedures/rock-vocal-no-scream.md`) / смена anchor / −5–10 BPM.

### 6. Стем-микс
- Выбрать одну stem-философию на весь релиз: якорь-король или стемы-заменяют.
- Coldwave-пресет 7 стемов: см. пакет `suno/packages/darksynth_coldwave.md` § Mix start.
- EQ/пан: `suno/stem_mixing.md`. Моно-проверка обязательна.

### 7. Мастеринг
- Цель по Платформа в карточке.
- Spotify default: -14 LUFS, ceiling ≈ -2 dBTP, crest 10–12.
- Post-master pro2/pro3 — см. `production/post_master_pipeline.md`. Не давить crest до 3.

### 8. Релиз
- Мета: название, EP, обложка, ссылка Suno / аудио.
- Статус Релиз только когда файл и мета готовы.

### 9. Postmortem (обязателен)
5 строк в поле Postmortem:
1. Что сработало в лирике
2. Что сработало в Suno-пакете
3. Что сломалось (визг / дыра в припеве / каша 1–3k / …)
4. Какой фикс помог
5. Куда урок лёг (какая страница KB / правка пакета)

Статус Postmortem → затем Архив.

---

## Команды агента

| Команда | Вход | Выход |
|---|---|---|
| `GENERATE` | бриф + плейбук | черновик лирики |
| `AUDIT` | текст | score + флаги |
| `REPAIR` | текст + флаги | правка ≤3 итераций |
| `PACKAGE` | готовый текст + плейбук | Style + Lyrics tags + anchor + negatives |
| `VOCAL FIX` | проблемный вокал | новый anchor / anti-scream блок |
| `MIX BRIEF` | плейбук + stem-философия | 7-stem уровни/пан/EQ-заметки |
| `MASTER TARGET` | платформа | LUFS/peak/crest цели |
| `POSTMORTEM` | карточка трека | 5 строк + предложения в KB |

---

## Правила канона (не ломать)

1. **Один хребет саунда на релиз** — не менять плейбук/stem-философию посередине EP.
2. **Канон > архив** — правим пакеты и эту страницу, а не плодим пятую энциклопедию.
3. **Нет postmortem — цикл не закрыт.**
4. Горизонтальный импорт из GitHub — только если закрывает дыру в одном из этапов.
5. R&D vs Shipping: экспериментальные якоря помечаем в Заметках; в shipping-EP только проверенные.

---

## Ссылки

- Пакеты: `suno/packages/darksynth_coldwave.md`, `suno/packages/folk_horror.md`, `suno/packages/cloud_bedroom.md`
- Кейсы: `cases/`
- Энциклопедия: `songwriting/encyclopedia.md` (§25–28: детектор + функция оценки)
- Жанровые плейбуки: `genres/folk_horror.md`, `genres/darksynth_coldwave.md`, `genres/cloud_bedroom.md`
- Золотой корпус: `references/golden_corpus.md` (14 регрессионных кейсов)
- Продакшен: `production/mixing.md`, `production/mastering.md`, `production/post_master_pipeline.md`, `production/coldwave_mix_mastering.md`
- Suno процедуры: `suno/procedures/generation-workflow.md`, `suno/procedures/rock-vocal-no-scream.md`

---

## 90 дней (напоминание)

- **М1 Склейка:** эта страница + база + 3 пакета — *сейчас*
- **М2 Калибровка:** 8–12 полных циклов, звуковой золотой корпус
- **М3 Shipping:** один цельный релиз + «Канон саунда ameobius» v1.0
