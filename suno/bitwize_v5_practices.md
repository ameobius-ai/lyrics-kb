# bitwize V5/V5.5 best practices — дистиллят новых ядер

> Источник: bitwize-music-studio/claude-ai-music-skills `reference/suno/v5-best-practices.md` (2026-08-04). Здесь только то, чего нет в blake_crosley_v55.md / t16_sngx_lite.md / style-tag-grammar.

## V5.5: движок слушает иначе

- V5.5 — эволюция V5: синтаксис/метатеги/структура/стиль-бокс 1000/лирика 5000 не менялись, ничего не deprecated
- Слайдеры творчества, голоса (Pro/Premier), Custom Models, My Taste — отдельные фичи
- Практика: **не переусложнять** — меньше овер-спекификации, 1-2 точных дескриптора вместо пяти мягких
- **Не переиспользовать V4/V4.5 промпты** (рекомендация CTO): V5 слушает буквально, старые промпты дают мусор

## Style-бокс: правило «синоним-кучи» вместо «4-7 дескрипторов»

- «4–7 дескрипторов» — НЕ официальное правило Suno (трассируется к одному стороннему гайду)
- Рабочие стиль-боксы спокойно бывают ~10 дескрипторов, если каждый делает своё дело
- Резать **синонимы**, не деталь: `intimate / breathy / whispery / soft` — это одна идея, оставить одну; но инструменты/вокал/продакшен-детали не выкидывать ради числа
- Плохо: vague («nice upbeat music») и synonym-pile; хорошо: «Sad indie folk, acoustic, gentle, breathy female vocal, intimate»

## Четырёхчастная анатомия стиль-бокса

1. Жанр + эпоха + влияния («90s alt-rock with Britpop undertones»)
2. Темп/ключ (120 BPM, A minor)
3. Инструментация/аранжировка (live drums, room ambience, palm-muted guitars)
4. Продакшен/микс (analog glue compression, tape saturation, lead vocal upfront)

Альтернатива: Top-Loaded Palette — `[Mood] + [Energy] + [2 инструмента] + [Вокальная идентичность]`

## Длины лирики (новое число)

- Цель **200–350 слов** для большинства жанров (до 500 — хип-хоп/рэп)
- Оптимум: 2 куплета + припев + бридж; избегать песен на 4-5 куплетов — Suno ускоряет/сжимает плотный текст

## Динамика по секциям (таблица)

| Секция | Динамика | Фразировка | Вибрато |
|---|---|---|---|
| Verse | Low | Tight | Minimal |
| Pre-Chorus | Rising | Shorter | Growing |
| Chorus | High/Open | Sustained | Full |
| Bridge | Variable | New texture | Altered |

## K-pop мини-лейн (в базе не было)

- Обязательно `K-pop` + `maximalist` + `glossy` + концепт; вокал первым: `mixed group vocals, layered harmonies, K-pop idol group` — mixed group vocals ключевой тег для группового звука
- Романизированный корейский через дефисы надёжнее для произношения: `Sa-rang-hae` не `Saranghae`; `[Clear Vocals]` при смешении языков
- Переключение жанра внутри песни — **родительскими ремарками на каждой секции**, не только в глобальном стиле: `[Verse 1] (Soft R&B groove...)` / `[Chorus] (Explosive EDM drop...)` / `[Rap Verse] (Aggressive trap flow, 808 bass)`
- Структура длиннее западной: Intro → V1 → Pre-Ch → Ch → Post-Ch → V2 → Pre-Ch → Ch → Rap Verse → Bridge → Dance Break → Final Chorus (key change up) → Outro
- `[Dance Break]` — с `(Instrumental, heavy beat)` и минимумом/пусто в лирике
- Финальный припев часто на полтона выше: `(key change up, maximum energy)`
- Частые проблемы: generic pop → добавить концепт-слова; соло вместо группы → mixed group vocals; нет свича → секционные ремарки; гарбл-корейский → дефисы + [Clear Vocals]

## Саунд-эффекты в скобках (категории)

- Human: `[laughter] [screaming] [whisper] [sigh] [gasp] [cough]`
- Crowd: `[crowd] [applause] [cheering]`
- Mechanical/transition: `[echo] [phone ringing]` — нарративный приём

## Честные оговорки

- «Улучшенная нюансировка/динамика V5.5» — заявлено движком, независимо не верифицировано
- Практика на K-pop-разделе — community-вывод, не официальный канон
