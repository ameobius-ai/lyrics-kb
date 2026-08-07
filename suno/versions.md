# Suno: версии

## Статус (проверено 2026-08-07)

- **Текущая стабильная модель — v5.5** (релиз 26.03.2026): Voices, Custom Models (от 6 треков каталога), My Taste; default в API (`chirp-fenix`). Free-план работает на v4.5-all.
- **v6 не анонсирован.** Suno подтверждает следующее поколение моделей в партнёрстве с музыкальной индустрией «позже в 2026»; имя, дата и набор фич не объявлены. В процедурах на v6 не закладываться.
- **Watch-item (06.08.2026)**: Suno вводит новую политику скачиваний, watermarking и transparency tools для идентификации AI-треков. К релизу проверить шаг 8 `pipeline/release_v1.md` — сейчас шага скачивания/лейблинга там нет, ломать нечего; возможно, появится обязательный лейбл AI-контента.

[источники: suno.com/release-notes, suno.com/blog/v5-5, help.suno.com model timeline, digitalmusicnews 06.08.2026 — см. issue #41]

---

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
