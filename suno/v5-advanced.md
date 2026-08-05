# Suno: v5.5 продвинутый фреймворк (T16.PRO)

Мост: акустическая физика ↔ когнитивные семантики Suno. Перевод продакшен-концепций в промпт-токены.

## §1 FREQ_SPACE_MS — Mid-Side локализация

**[MID_MONO] <100 Гц — моно-центр низа:**
```
"focused mono low-end, rock-solid center, driving localized sub-bass"
```
Держит ритм-секцию по центру, без фазового размытия.

**[SIDE_BOOST] >10 кГц — панорамный воздух:**
```
"ultra-wide panoramic air, shimmering stereo fields, immersive dimension"
```
Разводит эмбиент, тарелки, реверб-хвосты по краям.

**[DYNAMIC_MASKING_CARVE] 1-3 кГц — вокальный карман:**
```
"perfectly separated vocal pocket, pristine sonic hierarchy, non-overlapping clarity"
```
Изолирует лид-вокал от гитар/синтезаторов, предотвращает кашу.

**[PUMPING_SIDECHAIN] — сайдчейн:**
```
"interlocking groove, breathing rhythm, pumping sidechained bassline-kick integration"
```

## §2 DYNAMICS_ENVELOPE — транзиенты

**[SHARP_ATTACK] — острая атака:**
```
"crisp snapping attack, hyper-detailed transient definition, biting articulation"
```
Контекст: modern pop, metal, EDM, synthwave solos

**[SOFT_ATTACK] — мягкая атака / легато:**
```
"legato flowing textures, bowed organic sustain, smooth blurred transients"
```
Контекст: cinematic violin, dream-pop, shoegaze

**[STACCATO_GATED] — роботизированный срез:**
```
"staccato mechanical precision, gated robotic cuts, dry abrupt stopping"
```
Контекст: industrial, glitch, modern trap, phonk

**[INFINITE_DECAY] — бесконечный сустейн:**
```
"infinite blooming decay, long-releasing organic tails, bleeding notes"
```

## §3 MOD_TEXTURE_MAP — модуляция и саунд-дизайн

**[MICROSHIFT] — псевдо-даблтрек:**
```
"lush double-tracked vocal shimmer, thick liquid harmonization, wide space-chorus sheen"
```
Эффект дорогого «жирного» вокала без дублирования текста.

**[GRANULAR_GLITCH] — гранулярный синтез:**
```
"glitchy granular clouds, micro-sampled erratic textures, fragmented audio shards"
```

**[FORMANT_SHIFT] — тембральный сдвиг:**
```
"formant-shifted deep vocal shadows, ethereal pitched-up octave layers"
```

**[RESONANT_SWEEP] — фильтрация и фазеры:**
```
"swirling psychedelic movement, jet-stream filtering, sweeping resonant textures"
```

## §4 MACRO_TRANSITIONS — структурные теги (в поле Lyrics)

```
[Beat Switch]           → "abrupt structural shift, rhythm mutation"
[Dynamic Drop]          → "explosive bass-drop release, high-energy impact"
[Cinematic Breakdown]   → "stripped-back arrangement, naked acoustic core"
[Modulation Key Change] → "uplifting harmonic lift, rising emotional key"
[Glitched Outro]        → "digital system failure, stuttering deceleration, end"
```

## §5 HYBRID_ARCHETYPES — готовые пресеты

**ARCH_09 CYBER_MELODIC_TECHNO_VIOLIN (120-125 BPM):**
```
style: "cinematic melodic techno, driving cyberpunk 120 BPM, dramatic classical violin solo, lush grand hall wash, aggressive pumping sidechained bassline, sharp mechanical percussion, tension building, high-contrast dark neon atmosphere"
sliders: Weirdness 20% | Style 80% | Audio 25%
```

**ARCH_10 HYPERPOP_GLITCH_CORE (160 BPM):**
```
style: "hyperpop glitchcore, pitch-shifted digitized vocals, extreme hard autotune sheen, bitcrushed heavy 808 bass, frantic shattering transients, colorful chaotic digital distortion, 160 BPM"
sliders: Weirdness 65% | Style 55% | Audio 10%
```

**ARCH_11 DARK_DRIFT_PHONK:**
```
style: "dark drift phonk, distorted underground memphis vocal samples, heavy saturated 808 cowbells, gritty overdriven bassline, aggressive staccato mechanical beat, ominous late-night street atmosphere"
sliders: Weirdness 30% | Style 75% | Audio 45%
```

**ARCH_12 NEO-CLASSICAL_GLITCH_AMBIENT:**
```
style: "neo-classical glitch ambient, intimate close-mic felt piano, smooth legato strings, ethereal algorithmic shimmer reverb, micro-sampled erratic glitch textures, cinematic emotional depth, wide panoramic space"
sliders: Weirdness 50% | Style 60% | Audio 50%
```

## §6 COGNITIVE_INVERSE — эмоция → инженерия

| Эмоция/ТЗ | Промпт-фраза |
|---|---|
| Клаустрофобный, давящий | `claustrophobic mono production, compressed suffocating space, dark muffled tones` |
| Дорогой глянцевый релиз | `pristine high-end gloss, studio-polished radio-ready mix, impeccable sonic hierarchy, crystal-clear definition` |
| Психоделический трип | `swirling psychedelic movement, bouncing stereo delay echoes, melting liquid textures` |

## §7 Синтаксис v5.5

**RULE_01 COMPOUND_HYPHENATION — экономия символов:**
Поле Style = 120 символов. Дефисное объединение:
- ❌ `cinematic hall reverb wash with epic spatial depth` (51)
- ✅ `cinematic-hall-wash, epic-spatial-depth` (38)

**RULE_02 DYNAMIC_TAG_BRACKETING — вокал в скобках:**
Вокальные дескрипторы ВСЕГДА в скобках в начале поля стиля:
```
[polished upfront male vocal], darksynth, driving-groove...
```

**RULE_03 TRIAD OF CONTRAST — закон контраста:**
Формула: `[Сухой/Близкий центр] + [Глубокий/Размазанный бока]`
```
intimate close-mic dry vocal combined with grand-hall cinematic strings background
```

[источник: TG suno_promt_rus, faaatheeerrr (T16.PRO v2.0), 2026-06-15]
