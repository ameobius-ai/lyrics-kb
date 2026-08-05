# SiliconSense Guides — 10 гайдов по Suno v5.5

Источник: SiliconSense (siliconsense_dump). 10 полных гайдов с практическими
рецептами. Ниже — выжимка каждого, с ключевыми техниками.

---

## 1. Промпт-формула и key trick

**Формула:** `[Genre] · [Era] · [Instruments] · [Production] · [Vocals] · [Tempo / mood]`

Каждый блок контролирует один слой звука. Пропуск → Suno заполняет default
(обычно не в твою пользу).

**Key trick — style без artist names.** Suno блокирует имена артистов.
Фикс: разбить звук артиста на traits — era, signature instruments, vocal type,
delivery, production quirks. Получаешь звук без триггера фильтра.

Примеры (copy-paste в Style):
- Synthwave: `1980s synthwave, nostalgic cinematic mood, mid-tempo 110 BPM, analog poly-synth arpeggios, gated-reverb drums, fretless bass, warm male vocals with light reverb, neon night-drive atmosphere, polished retro production`
- Lo-fi: `lo-fi hip-hop, calm and study-friendly, ~80 BPM, dusty boom-bap drums, mellow Rhodes piano, soft upright bass, vinyl crackle, no vocals, rainy late-night mood, warm tape saturation`
- RU indie ballad: `melodic indie-pop ballad sung in Russian, melancholic and intimate, mid-tempo, fingerpicked acoustic guitar, warm synth pads, breathy male vocals, late-night atmosphere, clean modern production`

**v5.5 specifics:**
- Чище вокал и стерео. v5.5 держит vocal anchor лучше — описывай delivery ("breathy", "belting", "raspy"), не просто "male/female"
- Явный BPM ("92 BPM") → стабильнее чем "mid-tempo"
- Production tags: "tape saturation", "sidechain", "lo-fi", "polished" заметно меняют микс

**Ошибки:**
- Artist names → cut by filter
- Too generic ("pop song") → generic output
- Tag overload (15+) → diluted. Держи 5–8 блоков
- No vocal block → модель решает за тебя

---

## 2. Sound like any artist — без имени

Схема: `[Era] · [Genre] · [Instruments / gear] · [Production] · [Vocal character] · [Tempo]`

Чем специфичнее "era gear" (модель драм-машины, тип синта, трюк сведения),
тем ближе Suno попадает — без имён.

**Не работает:** `a song like [famous band]`
**Работает:** `1980s synth-pop, glossy analog synths, gated reverb snare, drum machine, soaring emotive male vocals with reverb, anthemic chorus, 118 BPM`

Вокал — половина узнаваемости. Добавляй dedicated anchor block (timbre, delivery, texture).

---

## 3. Persona — тот же голос между песнями

Suno Studio update (early 2026). Persona фиксирует голос трека и переносит
на новые.

**Создание:**
1. Сгенерируй пока не получишь вокал который нравится
2. Открой трек → `•••` → "Create Persona"
3. Дай имя (напр. "Night Baritone")
4. В новой песне выбери Persona — Suno переиспользует голос

**Persona + delivery tags = контроль.** Persona держит тембр, delivery tags
в Lyrics управляют как он поёт в каждой секции:

```
[Verse 1]
[Whispered]
soft, intimate verse

[Pre-Chorus]
[Build]

[Chorus]
[Belted]
a powerful belt on the chorus

[Bridge]
[Soft]
a dip before the finale
```

**Лимиты:** не точная копия. Якорь — голос близок, не идентичен трек к треку.

---

## 4. Repeatability — тот же промпт, стабильный результат

Suno вероятностный. Нет публично контролируемого seed. Но дисперсию можно сузить.

**Lever 1 — детальный промпт.** Чем конкретнее, тем меньше свободы у модели.
- Vague: `pop song, sad` → max variance
- Specific: `melancholic indie-pop, 92 BPM, A minor key, fingerpicked acoustic guitar, warm synth pads, breathy male vocals, no autotune, intimate late-night mix` → stable

**Lever 2 — Persona для голоса.** Главный источник "другой певец каждый раз" — вокал.
Save → apply to new tracks.

**Lever 3 — generate and curate.**
- Генерируй несколько вариантов, выбери лучшее — это нормальный workflow
- Extend от хорошего take — сохраняет характер
- Явный BPM и key резко снижают tempo/harmony wobble

---

## 5. Chord progression — аккорды в квадратных скобках

Аккорд в `[]` перед строкой в Lyrics → Suno читает как harmony instruction.
В Style — добавь key, держит гармонию в правильной шкале.

**Пример (Am–F–C–G в A minor):**
```
[Verse 1]
[Am] City sleeps and [F] I am wide awake
[C] Streetlights at the [G] window tremble soft

[Chorus]
[Am] Call me up now, [F] call me back
[C] Through the years and [G] through the days
```
Style: `melancholic indie-pop, acoustic guitar, 90 BPM, warm male vocals, A minor key`

**Работает:** простые triads (Am, F, C, G, Dm, Em) + common progressions в одной тональности.
Bracketed chords + key in Style → резко повышает hit rate.
**Не работает:** complex jazz chords, extended chords, mid-song key changes, voicings/inversions.
Вероятностный трюк — best shot, не 100%.

---

## 6. Extend — длинный трек

**Почему короткий:** Suno строит музыку из Lyrics box. Один verse + chorus →
модели нечего "играть", трек заканчивается. Length = amount of text + section tagging.

**Method 1 — полная структура сразу:**
```
[Intro]
[Verse 1]
[Pre-Chorus]
[Chorus]
[Verse 2]
[Chorus]
[Bridge]
[Chorus]
[Outro]
```

**Method 2 — Extend:**
- Open finished track → Extend — модель продолжает с конца
- Повторяй Extend несколько раз
- Добавляй следующие секции в каждое продолжение ([Verse 2], [Bridge], [Outro])
- **Всегда** заканчивай явным `[Outro]` — иначе трек может оборваться mid-phrase

**Дрифт на Extend:** повторяй тот же style prompt, фиксируй вокал Persona,
не меняй жанр между частями → куски сшиваются в один трек.

---

## 7. Russian names & brands — транслитерация

Suno обучен на английском, читает русский "по буквам", незнакомые proper nouns
заполняет English-style phonetics → "Spotify" звучит неузнаваемо.

**Фикс — кириллицей по звуку:**
- Spotify → Спотифай
- YouTube → Ютуб
- iPhone → Айфон
- weekend → уикенд
- online → онлайн
- 2026 → две тысячи двадцать шесть

**Имена/фамилии:**
- Пиши фонетически как должно звучать
- Разделяй по слогам длинные/ambiguous имена если вокал спотыкается
- Ставь ударение на нужную гласную — модель перестаёт гадать
- Числа — словами

---

## 8. Russian lyrics — ударения, произношение, чистый вокал

Три типичные проблемы: wrong stress, swallowed endings, consonant mush в длинных словах.

**Что помогает:**
- Stress mark над гласной в ambiguous словах — модель перестаёт гадать
- Разделяй длинные слова по слогам где вокал спотыкается
- Избегай heavy consonant clusters на стыках слов — перефразируй
- Числа и Latin — словами

**Автоматизация:** Russian Lyrics Prep tool — маркирует ударения, разделяет
проблемные слова, флагает рискованные комбинации. Meaning и rhyme сохраняются.

Tip: pick a Russian-language vocal-style preset for delivery — убирает половину
pronunciation issues до генерации.

---

## 9. Song structure — meta tags

**Core:** `[Intro]`, `[Verse]` (нумеруй: [Verse 1], [Verse 2]), `[Pre-Chorus]`,
`[Chorus]` (повторяй перед каждым возвратом), `[Bridge]`, `[Outro]`,
`[Instrumental]`, `[Break]`.

**Advanced (v5/v5.5):** `[Build]`, `[Drop]`, `[Whispered]`, `[Belted]`,
`[Guitar Solo]`, `[Sax Solo]`, `[Female Vocal]`, `[Male Vocal]`.

Без тегов Suno решает сам где verse/chorus — рубит, повторяет, переставляет.
Теги в `[]` в Lyrics задают скелет.

**Classic pop/rock skeleton:**
```
[Intro]
[Verse 1]
[Pre-Chorus]
[Chorus]
[Verse 2]
[Pre-Chorus]
[Chorus]
[Bridge]
[Chorus]
[Outro]
```

---

## 10. Upload rejected — "already in our database"

Suno считает acoustic fingerprint при загрузке. Если похож на что-то в базе —
блок. Даже на свои оригиналы: similar arrangement, previous upload, shared sample.

**Фикс — измени аудио достаточно чтобы fingerprint стал другим, мелодия осталась:**
- Pitch shift 1–2 semitones (keep tempo)
- Tempo shift / slight time-stretch
- Micro-EQ и saturation
- Trim to 60–120 sec — короткие фрагменты проходят чаще

Обработанный файл звучит слегка искажённым — это ожидаемо: Suno использует его
как melody reference и генерирует чистый трек.

---

## Связь с базой

- `suno/prompts.md` — meta-tags, style tag категории
- `suno/v5-advanced.md` — v5.5 фреймворк, синтаксис
- `suno/persona.md` — дрейф персоны (наша запись)
- `suno/vocal_anchors.md` — 24 вокальных блока
- `suno/behavior_tags.md` — 48 поведенческих тегов
- `suno/genre_bpm_map.md` — 420 жанров с BPM
- `suno/arrangement.md` — пропадающие инструменты в припеве
