# lyrics-kb

База знаний по сонграйтингу и звуку музыкального хаба.

**Правило зеркала:** источник правды — Notion (карточки базы «Треки и релизы» + канон-страницы в «Плейбуках»). Этот репозиторий — зеркало для кейсов и референсов, а не второй источник правды.

## Структура

- `cases/` — кейсы треков: лирика-аудит, метрики, fail_mode, урок. Именование: `{LANE}-{NNN}-{slug}.md`
- `references/` — справочники по всем кейсам: `sound_corpus.md` (звуковые метрики и таргеты) · `swamp-lane.md` (хаб болотной полосы) · `release-pipeline-v1.md` (канон пайплайна) · `blake_crosley_v55.md` (дистиллят Suno V5.5: метатеги, слайдеры, стемы, траблшутинг) · `blake_crosley_suno_guide_v55.md` (полный гайд Blake Crosley, 110k, обновлён 2026-07-25)
- `suno/` — пакеты Style / behavior-тегов: `style-tag-grammar.md` (канон всех лейнов) + per-lane `coldwave.md` · `swamp.md` · `industrial.md` · `metalcore.md`
- `songwriting/` — сонграйтинг-канон: `anti-patterns.md` · `top-texts-teardown.md` · `cw-lessons.md` · `swamp-playbook.md` · `industrial-danger-levers.md` · `en/EN_CRAFT_LAYER.md` · `ru/` (энциклопедия, 4 части)

## Лейны

| Код | Лейн |
|---|---|
| CW | darksynth / coldwave |
| SWP | болотный фолк-электроник |
| IND | industrial / neurofunk |
| MC | металкор / пост-хардкор |
| FH | фолк-хоррор |

## Кейсы (12)

| Файл | Трек | Score | Статус |
|---|---|---|---|
| `cases/CW-001-poslednee-okno.md` | ПОСЛЕДНЕЕ ОКНО | 8.1 | CLOSED, калибровка серии |
| `cases/CW-002-trista-sorok-sem.md` | ГИЛЬОТИНА / ТРИСТА СОРОК СЕМЬ | 8.4 | CLOSED, result good |
| `cases/CW-003-razmorozka.md` | РАЗМОРОЗКА | 8.3 | Генерация |
| `cases/CW-004-chuzhoy-etazh.md` | ЧУЖОЙ ЭТАЖ | 8.1 | Генерация |
| `cases/CW-005-schetchik.md` | СЧЁТЧИК | 8.2 | Генерация |
| `cases/SWP-010-mara.md` | МАРА | 8.6 | Генерация |
| `cases/SWP-011-shishiga.md` | ШИШИГА | 8.5 | Генерация |
| `cases/SWP-012-staritsa.md` | СТАРИЦА | 8.6 | Генерация |
| `cases/SWP-013-bylichka.md` | БЫЛИЧКА | 8.7 | Генерация · максимум хаба |
| `cases/IND-001-third-pass.md` | THIRD PASS | 8.4 | GEN READY |
| `cases/IND-002-kill-the-crest.md` | KILL THE CREST | 8.3 | GEN READY |
| `cases/MC-001-toxic.md` | TOXIC | 7.6 → 8.6 | Мастеринг (over_master) |

## Статус зеркала (2026-08-02)

Зеркало собрано: 12 кейсов, 3 референса, 5 suno-файлов, 6 файлов сонграйтинг-канона + энциклопедия в 4 частях (`songwriting/ru/`). Дальше — режим поддержки: новые кейсы и правки канона идут сюда следом за Notion.

Открытый хвост: §22–27 энциклопедии (AI-карта, деревья, векторы, паттерны, трансформации, шаблоны) — догрузить отдельным проходом.

Исторический долг закрыт: файл `cases/CW-012-tri-cifry.md` со старого репо здесь не воссоздаётся — кейс сразу лежит под правильным именем. Из старого репо не перенесены: `cases/EN-001…EN-010`, `suno/genre_bpm_map.md`, `suno/persona.md`, `references/siliconsense_genre_bpm.json` — судьба решается человеком (см. ишью в Notion).