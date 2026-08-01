# lyrics-kb

База знаний по сонграйтингу и звуку музыкального хаба.

**Правило зеркала:** источник правды — Notion (карточки базы «Треки и релизы» + канон-страницы в «Плейбуках»). Этот репозиторий — зеркало для кейсов и референсов, а не второй источник правды.

## Структура

- `cases/` — кейсы треков: лирика-аудит, метрики, fail_mode, урок. Именование: `{LANE}-{NNN}-{slug}.md` (`CW-002-trista-sorok-sem.md`, `SWP-010-mara.md`, `IND-001-…`)
- `references/` — справочники, сведённые по всем кейсам (`sound_corpus.md` — звуковые метрики и таргеты; `swamp-lane.md` — хаб болотной полосы)
- `suno/` — пакеты Style / behavior-тегов: `style-tag-grammar.md` (канон всех лейнов) + per-lane `coldwave.md` · `swamp.md` · `industrial.md` · `metalcore.md`

## Лейны

| Код | Лейн |
|---|---|
| CW | darksynth / coldwave |
| SWP | болотный фолк-электроник |
| IND | industrial / neurofunk |
| MC | металкор / пост-хардкор |
| FH | фолк-хоррор |

## Статус зеркала (2026-08-01)

- [x] `cases/CW-002…CW-005` (4 кейса)
- [x] `cases/SWP-010…SWP-013` (ГАТЬ, 4 кейса)
- [x] `references/sound_corpus.md` v0.1
- [x] `references/swamp-lane.md`
- [x] `suno/style-tag-grammar.md`
- [x] `suno/coldwave.md` · `suno/swamp.md` · `suno/industrial.md` · `suno/metalcore.md`

Зеркало собрано полностью. Дальше — режим поддержки: новые кейсы и правки канона идут сюда следом за Notion.

Исторический долг закрыт: файл `cases/CW-012-tri-cifry.md` со старого репо здесь не воссоздаётся — кейс сразу лежит под правильным именем.