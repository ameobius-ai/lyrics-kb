# Behavior Tags — 48 тегов: поведение вместо «тупых» меток

Источник: SiliconSense (siliconsense_dump). 6 категорий, 48 тегов.
Ключевая идея: `[Structure: Anthemic Peak]` говорит секции **что делать**,
а не просто как называться. `[Verse]`/`[Chorus]` — blunt, часто форсят generic-pop.

## STRUCTURE (10) — поведенческие структурные теги

| тег | что делает |
|---|---|
| `[Structure: Focused Performance]` | Tight storytelling, medium energy |
| `[Structure: Build-up]` | Rising tension, instruments layering in |
| `[Structure: Anthemic Peak]` | Track's biggest moment, peak hook energy |
| `[Structure: Minimalist Breakdown]` | Stripped down intimacy, lots of space, few instruments |
| `[Structure: Cinematic Drop]` | Cinematic dramatic hit after pause |
| `[Structure: Outro Fade]` | Gradual track fade-out |
| `[Structure: Spoken Bridge]` | Spoken bridge instead of a melodic section |
| `[Structure: Call and Response]` | Two voices/instruments trading lines |

> `[Verse]` и `[Chorus]` остаются как маркеры секций, но behavior-теги добавляются
> рядом чтобы задать **поведение** секции, а не только её название.

## PIPE COMBINATIONS (5) — комбинированные теги через `|`

Синтаксис: `[Секция | Поведение | Эффект | Инструмент]`

| тег | описание |
|---|---|
| `[Chorus | High Energy | Anthemic | Electric Guitar Solo]` | Anthem chorus + guitar solo |
| `[Verse | Whispered | Close-mic | Sparse Drums]` | Whispered intimate verse |
| `[Bridge | Half-time | 808 sub bass | Vinyl static]` | Half-time bridge with trap bass |
| `[Pre-chorus | Build-up | Rolling Toms | Crescendo]` | Build-up to chorus |
| `[Drop | Distorted Guitar | Stadium crowd ambience]` | Big stadium drop |

## INSTRUMENTS (Meta Tags) (11) — переключение инструментов

| тег | что делает |
|---|---|
| `[Rhodes]` | Warm electric piano |
| `[Synth Pad]` | Atmospheric synth wash |
| `[Distorted Guitar]` | Switch into distorted guitar |
| `[Slap Bass]` | Funky slap bass |
| `[Banjo]` | Banjo for country/americana |
| `[Mellotron]` | Vintage flute/string pad |
| `[Taiko Drums]` | Thunderous taiko drums |
| `[Brass Section]` | Brass horns |
| `[Strings Section]` | Symphonic string section |
| `[Choir Vocals]` | Choir backing |
| `[Breakbeat]` | Sampled funk break |

## VOCAL EFFECTS (8) — эффекты на вокал

| тег | что делает |
|---|---|
| `[Whispered]` | Whisper this line |
| `[Autotuned]` | Hard Auto-Tune |
| `[Powerful]` | Powerful belt |
| `[Doubled]` | Double the vocal |
| `[Megaphone]` | Megaphone distortion |
| `[Vocal Chops]` | Chopped vocal samples |
| `[Talkbox]` | Talkbox effect |
| `[Ad-libs]` | Spontaneous backing yells |

## ATMOSPHERE & PRODUCTION (10) — атмосфера и продакшен

| тег | что делает |
|---|---|
| `[Rain]` | Rain sound |
| `[Vinyl static]` | Vinyl crackle |
| `[Stadium crowd ambience]` | Stadium crowd |
| `[Tape saturation]` | Analog tape saturation |
| `[Lo-fi 4-track]` | Lo-fi 4-track recording |
| `[Plate reverb]` | Plate reverb |
| `[Sidechain pump]` | Sidechain pumping |
| `[Silence]` | Silence / pause |
| `[Drum fill transition into chorus]` | Drum fill into chorus |
| `[Smooth crossfade intro to verse]` | Smooth crossfade into verse |

## Full structure example — пример песни с behavior tags

```
[Verse 1]
[Structure: Focused Performance]
[Vocal: female, smooth and soulful, airy on quiet lines, powerful belting on peaks]

[Pre-Chorus]
[Structure: Build-up | Rolling Toms]
Bassline creeps in slow, heart starts to race...

[Chorus]
[Structure: Anthemic Peak | Stadium crowd ambience | Choir Vocals]
Rise up — break free — let the whole block hear you roar...

[Bridge]
[Structure: Minimalist Breakdown | Rain | Silence]
Just breath... and echoes... fading in the rain...
```

## Как использовать

- Behavior tags ставятся **в Lyrics box**, не в Style
- Можно комбинировать с классическими `[Verse]`/`[Chorus]` — они задают позицию,
  behavior-тег задаёт **что происходит**
- Pipe-комбинации `[A | B | C | D]` — компактный способ задать несколько аспектов
- `Silence` и `Rain` — атмосфера работает как инструмент, пауза тоже музыка

## Связь с базой

- `suno/prompts.md` — meta-tags структура
- `suno/v5-advanced.md` — v5.5 синтаксис, triad of contrast
- `suno/arrangement.md` — фикс пропадающих инструментов
