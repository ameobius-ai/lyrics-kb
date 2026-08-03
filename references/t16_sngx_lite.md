# T16-SNGX-LITE v1.2 — дистиллят (переводчик «пожелание → Suno-пакет»)

> Источник: системный промпт для Qwen Studio 3.7 «T16-SNGX-LITE v1.2» (Telegram, 2026-08-04, файл `T16-SNGX-LITE v1 3.md`).
> Статус: **community-промпт, непроверенный** (v1.1/v1.2 — фиксы собственных логических ошибок). Каноном НЕ называем.
> Ценность: Exclude-матрица, словарь «железо → дескрипторы», гейт TERM_LEAK_SCAN, идея Defense Layers.

## Концепция

Сырое пожелание (техтермины, бренды, референсы) → пакет из ТРЁХ блоков:
1. **STYLE** — ≤200 символов, 6-9 фраз, вокал первым (GMIV-порядок)
2. **EXCLUDE** — готовый список для поля Exclude (Advanced Options), из матрицы+пола, не с нуля
3. **LYRICS** — построчно по секциям, каждая секция имеет style-строку + lyric-строки

## GMIV — порядок сборки STYLE

VOCAL (пол+регистр+манера) → ЖАНР+ПОДЖАНР+ЭПОХА → НАСТРОЕНИЕ (2-3, без синонимов) → ИНСТРУМЕНТЫ (2-3 + прилагательное) → ТЕКСТУРА+ЧИСТОТА (по 1) → BPM+язык.

**⚠ Спорно:** вокал ПЕРВЫМ — у нас и у Blake Crosley жанр первым. Проверять на практике, не брать на веру.

Тег-пулы (вокал/настроение/чистота/инструмент+прил/текстура) — стандартные Suno-дескрипторы, ничего волшебного.

**Conflict check:** чистые дескрипторы (pristine/polished/hi-fi/crisp) конфликтуют с lo-fi/muddy/raw. Хочет lo-fi → НЕ добавлять cleanliness-слово, брать компромисс («warm tape saturation»/«controlled vintage character»), предупредить юзера.

## TERM_LEAK_SCAN (гейт для STYLE)

Проверить черновик STYLE: цифра+Hz/kHz/dB/ms вне слота BPM; капитализированные слова вне жанра/настроения/инструмента; имена артистов/продюсеров; плагины/DAW/железо. Найдено → перевести по словарю/fallback → переписать → пересканировать. Без исключений.
= наш запрет брендов/Hz/имён в style, оформленный как блокирующий чек.

## EXCLUDE — Archetype Baseline Matrix (ценное)

**Universal MIX Floor (всегда):** `muddy-low-end, over-compressed, flat-dynamics, harsh-highs`
(для lo-fi-запроса — оставить только flat-dynamics, остальное по Conflict check)

Брать строку архетипа за базу, корректировать под явные пожелания:

| Архетип | INSTRUMENTS | VOCAL | DRUMS | PRODUCTION | FX |
|---|---|---|---|---|---|
| Ballad/intimate | distorted-guitars, metal-riffs, full-orchestra* | hard-autotune, screamo, growl | trap/808/edm-kick | trap-elements, reggaeton-beat | heavy-distortion, bitcrush |
| Pop upbeat | shred-guitar, hand-drums* | growl, operatic-wail | blast-beat, double-kick | vintage-tape-degr.* | cathedral-reverb |
| EDM/House | full-orchestra, strings, brass* | melisma, operatic-wail | live-drums/perc | 90s-dry, blues-shuffle | spring-reverb |
| Hip-hop/Trap | full-orchestra, strings, timpani* | operatic-wail, children-choir | live-crowd, stadium-reverb* | jazz-swing, country-twang | cathedral-reverb |
| Rock/Metal | preset-synth, detuned-pad* | hard-autotune, chipmunk | 808/edm-kick, drum-machine | reggaeton-beat, trap-elements | bitcrush |
| Cinematic/Orch | distorted-guitars, power-chords | autotune, hard-autotune | 808/trap/edm-kick | trap-elements, reggaeton-beat | bitcrush, aliasing |
| Folk/Country | distorted-guitars, metal-riffs, preset-synth | hard-autotune, growl | 808/trap/edm-kick | trap-elements, reggaeton-beat | bitcrush |
| R&B/Soul | shred-guitar, power-chords | screamo, growl | blast-beat, double-kick | 80s-gated-reverb* | full-track-glitch |

`*` = условно, убрать если юзер явно хочет. Гибрид: объединить строки + MIX Floor, оставить 3-6 релевантных. Итог: MIX Floor + минимум 1 пункт в ≥3 из 5 категорий.

**Статус:** Exclude поле — реальная фича Suno (подтверждено Blake Crosley). Матрица — гипотеза автора, как baseline для старта ок, но не верифицирована.

## Словарь «железо → Suno-дескрипторы» (дополнение к engineering bridge)

- **Freq**: 100/30/55Hz sub→«deep controlled sub bass»; 200-500Hz mud→«tight clean low-mid»; 3-5k→«bright crisp attack»; air/10k+→«crystalline airy top»; HPF→«tight natural low»; LPF/dark→«muffled lo-fi rolloff»
- **Comp**: LA-2A/opto→«smooth leveled warm»; 1176/FET→«punchy in-your-face»; SSL/VCA→«modern glue tight»; parallel/NY→«massive explosive/punchy cohesion»; over-compressed→«flat dynamics» (в EXCLUDE!)
- **Sat**: tape→«warm analog soft-top»; tube→«rich harmonic valve warmth»; transistor→«gritty odd-harm»; distortion→«natural grit/controlled breakup»
- **Reverb/Delay**: plate→«vintage shimmer vocal-tail»; hall→«cinematic grand depth»; room→«intimate close live»; slap→«short stereo intimate»; ping-pong→«wide stereo bounce»; shimmer→«ethereal celestial wash»
- **Mics**: U47 close→«close-mic intimate warm»; SM58/dynamic→«tight dry vocal»; ribbon→«smooth dark vintage»; condenser→«detailed transparent hi-fi»
- **Drums**: DW/punchy→«punchy acoustic deep resonant»; 808→«deep controlled sub»; live→«natural acoustic transparent»; brushed→«brushed intimate»
- **Guitar**: Martin→«deep warm acoustic»; Tele→«twangy bright electric»; Les Paul→«thick rich warm electric»; Strat→«clean shimmering electric»; drop-D→«low-tuned deep resonant»
- **FX**: autotune→«smooth natural»/«hard-tuned zero-glide»; vocoder→«formant-shifted robotic stack»; bitcrush→«lo-fi glitchy chiptune»; OTT→«balanced polished wide-spectrum»
- **Fallback**: неизвестный бренд → классифицировать по функции (mic/comp/sat/verb/delay/synth/guitar/drum/vocal-FX) → логика ближайшей категории. Утилитарное железо (интерфейсы/кабели/DAW/ОС) = выбросить.

## Defense Layers (для >120с — идея, с оговоркой)

7 слоёв quality-якорей по РОЛИ секции (не по таймкоду — Suno не парсит секунды как метроном, это подтверждено):

- L1→INTRO: энергия 15-20%, якорь вокала/тембра, `quality:anchor pristine`
- L2→ПЕРВЫЙ VERSE: `quality:maintain clarity/mix/вокал`
- L3→ПЕРВЫЙ CHORUS: `quality:refresh+callback:как в intro+avoid:muffled,washed,smeared,harsh,muddy`
- L4→BREAKDOWN→RE-ENTRY: `quality:reset pristine` → `quality:re-entry full-band pristine` (чекпоинт)
- L5→пред-финальный build: `quality:lock full-spectrum, complexity_spike key+1`
- L6→ФИНАЛЬНЫЙ CHORUS: `quality:vocal_identity_final, climax 95-100%`
- L7→OUTRO: `quality:callback opening, fade-warmth`

Минимальная структура → L1,L3,L7. Полная → все 7. Нет breakdown → пропустить L4, не выдумывать.

**⚠ КРИТИЧЕСКАЯ ОГОВОРКА:** формат `[quality: ...]` — квадратные скобки ВНУТРИ LYRICS. По нашему знанию Suno ПОЁТ любые [brackets] кроме структурных тегов. Если эти строки уходят в Lyrics поле как есть — споёт мусор. В промпте это внутренний формат для Qwen (переводчика), финальная транскрипция в Suno-промпт неясна. **НЕ использовать `[quality:...]` в реальной лирике без проверки на генерации.**

## Прочее

- **Energy Ladder (>120с):** Intro/Outro 10-20 | Verse 30-45 | Pre-Chorus 55-70 | Chorus 85-95 | Bridge 25-40 (сброс) | Build 75-85 | Final Chorus 95-100. Не держать плоско выше 75 дольше 2:00.
- **GENERATION_STRATEGY (>120с):** честно сказать «Suno деградирует на длинных генерациях, ошибки копятся авторегрессивно». Варианты: один проход (принять риск) / сегментами 60-90с с реального структурного рубежа (граница первого припева/breakdown) / тестовый клип 30-45с. Выбор за юзером.
- **Risk Tiers:** T1 (>80%) стандартное <3:00; T2 (50-70%) >3:00, мультиязык, pristine на сложных жанрах; T3 (<30%) смена тембра, копия артиста, >5:00. T2/T3 → предупредить до генерации.
- LYRICS ≤4800 символов; каждый трек возвращается всеми тремя блоками, ни один не опускать.
