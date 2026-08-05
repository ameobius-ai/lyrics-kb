# Suno: версии

## v3.5
- Сырее, грубее
- Иногда нужнее когда нужна фактура а не чистота
- Меньше контроля

## v4
- Более чистый вокал
- Лучше структура
- Стабильнее

## v4.5
- Самый чистый вокал
- Лучший контроль
- Активно в ходу в сообществе (по состоянию на июнь 2026)
- Выбор по умолчанию для большинства задач

## v5.5
- Новое поколение, продвинутый синтаксис промптов
- Считывает структурные теги переломов ([Beat Switch], [Dynamic Drop], [Cinematic Breakdown], [Modulation Key Change], [Glitched Outro])
- Compound descriptors (дефисное объединение для 120-символьного лимита)
- Better instrument separation / панорама
- Sliders: Weirdness / Style / Audio — тонкая настройка
- Тестится в сообществе, фреймворки пишутся (T16.PRO)

## Model keys (API)

| Display | External Key | Default | Max Prompt | Max Tags |
|---------|-------------|---------|------------|----------|
| v5.5 | `chirp-fenix` | **YES** | 5000 | 1000 |
| v5 | `chirp-crow` | No | 5000 | 1000 |
| v4.5+ | `chirp-bluejay` | No | 5000 | 1000 |
| v4.5 | `chirp-auk` | No | 5000 | 1000 |
| v4.5-all | `chirp-auk-turbo` | Free | 5000 | 1000 |
| v4 | `chirp-v4` | No | 3000 | 200 |
| v3.5 | `chirp-v3-5` | No | 3000 | 200 |
| v3 | `chirp-v3-0` | No | 1250 | 200 |

Remaster: `chirp-flounder` (v5.5), `chirp-carp` (v5), `chirp-bass` (v4.5+)

[source: paperfoot/suno-cli API_INTELLIGENCE.md, verified 2026-07-18]

---

[источник: практика + TG suno_promt_rus, 2026-06]
