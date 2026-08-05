# 🦀 База знаний: русскоязычная лирика, сонграйтинг, продакшен и AI-промптинг

Рабочая база знаний для AI-музыкантов и продюсеров: **лирика → саунд-дизайн → промптинг → продакшен → мастеринг**.

## Что внутри

**101 запись, 8 категорий:**

| Категория | Файлов | Описание |
|---|---|---|
| `suno/` | 35 | Промпт-инженерия (meta-tags, style tags, behavior tags), версии (v3.5→v5.5), вокал-якоря (24), genre→BPM (420 жанров), **packages** (9 жанровых пакетов), procedures, **lanes** (style-tag-grammar + coldwave/industrial/metalcore/swamp из зеркала lyrics-kb), T16-SNGX-LITE, Blake Crosley V5.5 |
| `production/` | 8 | Сведение, мастеринг (LUFS, streaming), openDAW DSP (111 скриптов), BandLab пресеты, post-master pipeline (pro2/pro3), coldwave 7-stem mix, QC gate |
| `vocals/` | 1 | Типы голоса, регистры, обработка |
| `genres/` | 4 | Фолк-хоррор (плейбук), darksynth/coldwave (плейбук), саундклауд-волна (плейбук), общие жанровые характеристики |
| `songwriting/` | 15 | Энциклопедия v2.0, современная русская лирика, демо-EP + из зеркала lyrics-kb: анти-паттерны, CW-уроки, industrial levers, болотный плейбук, разбор топ-текстов, EN CRAFT LAYER, энциклопедия RU (4 части), Детектор 2.0 |
| `references/` | 18 | Пантеон 2.0, разведка сцены, золотой корпус, SiliconSense каталоги, writing craft books, звуковой корпус (sound_corpus), swamp-lane, release-pipeline-v1, Blake Crosley полный гайд, GigaChat интеграция |
| `pipeline/` | 1 | Release pipeline v1 — канон end-to-end (бриф→лирика→детектор→пакет→генерация→микс→мастер→релиз→postmortem) |
| `cases/` | 19 | Sound-cases: CW-001..014 (локальные + зеркальные CW-002..009), IND-001/002, MC-001, SWP-010..013 |

## Пайплайн

### Лирика → детекция → оценка

```
Энциклопедия v2.0 (30 разделов)
    ↓
Детектор 2.0 (25 паттернов + white-list 25.27 + hard-fail)
    ↓
3 жанровых плейбука (фолк-хоррор / darksynth / саундклауд-волна)
    ↓
Золотой корпус (14 регрессионных кейсов, FP=0 FN=0)
    ↓
Пантеон 2.0 + blend-карта → разведка сцены
```

### Промптинг → генерация → продакшен

```
Suno промпт-инженерия (meta-tags, style tags, vocal anchors, behavior tags)
    ↓
Genre→BPM карта (420 жанров) + 865 артистов (name-free style prompts)
    ↓
Генерация (procedures: workflow, v5 framework, vocal fix, arrangement fix)
    ↓
suno/packages/* → generation → cases/
    ↓
Стем-микс (Suno Studio, 6-полосный EQ, панорама, моно-проверка)
    ↓
Постобработка (FlashSR, BS-Roformer, MIDI extraction)
    ↓
Мастеринг (post-master pro2/pro3, BandLab пресеты, LUFS по платформам)
```

### Энциклопедия v2.0 (`songwriting/encyclopedia.md`)

30 разделов: теория (пантеон, метрика, рифма, структура, образы, синтаксис, голос, регистры, уродливое, звукопись, интертекст, 10 жанров, хук, explicit, сленг, анти-AI) + AI-операционная карта (детектор, трансформации, функция оценки, скаффолды).

**Детектор 2.0:** 25 паттернов AI-маркеров с весами, hard-fail правило (вес 2.0 → cap SUSPECT), white-list 25.27 (причитное усечение, припев-формула с накоплением).

**Функция оценки 2.0:** 12 параметров (P1–P12), жанровые веса по 6 жанрам, REPAIR-приоритизация, delta-формат.

### Жанровые плейбуки

- **Фолк-хоррор** (`genres/folk_horror.md`) — быт+миф=жуть, двухсловарная лексика, мифологемы
- **Darksynth/Coldwave** (`genres/darksynth_coldwave.md`) — холодный неон, разговорный синтаксис
- **Саундклауд-волна** (`genres/cloud_bedroom.md`) — спальник+интернет+самоирония

### Золотой корпус (`references/golden_corpus.md`)

14 тест-кейсов: 3 живых эталона, 6 слопов, 5 пограничных (white-list ловушки). Регрессионный протокол: FP=0, FN≤1.

## Валидация

```bash
python3 validate.py
```

Проверяет: JSON валидность, соответствие count, наличие всех файлов, отсутствие дублей.

## Источники

- Telegram: SUNO ПРОМПТ от @sergiyp, SUNO Лоджия
- Discord: Producers (guild 1506284805464260648)
- Notion: рабочие страницы (энциклопедия, детектор, плейбуки, корпус)
- Практика и собственный ресёрч

## Sync (Notion ↔ Git)

| Content | Master | Slave |
|---|---|---|
| pipeline, packages, golden corpus rules, encyclopedia KB | **Git** | Notion mirror |
| Track board, draft lyrics WIP, personal postmortems | **Notion** | export to cases/ only when closed |

Last sync: 2026-07-11
Notion-only: Треки/Релизы board, agent threads

## Лицензия

CC BY-NC 4.0 — некоммерческое использование с атрибуцией.
