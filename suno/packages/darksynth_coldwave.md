# Suno Package: Darksynth / Coldwave

Готовый релизный пакет под `genres/darksynth_coldwave.md`. Копировать в Style / Lyrics, не собирать с нуля.

[источник: Notion, 2026-07-11. Playbook: `genres/darksynth_coldwave.md`]

---

## Profile

| Параметр | Значение |
|---|---|
| BPM | 105–115 (якорь **110**) |
| Тональность (типично) | Am / Em |
| Вокал | deep baritone, чуть подтоплен |
| Stem-философия (default) | якорь-король |
| Платформа default | Spotify -14 |
| Референсы саунда | Molchat Doma, Boy Harsher, She Past Away |

## Style

```
[Vocal: male, deep husky timbre, relaxed but intense delivery, clear diction, precise rhythm, modern rap-adjacent tone], darksynth, coldwave, overdriven-bass, palm-mute-guitar, analog-arps, gated-snare, 110 BPM, intimate close-mic dry vocal combined with wide cold reverb wash, focused mono low-end, no screaming, no shouting, no vocal acrobatics
```

## Style compact

```
[deep husky baritone], darksynth, coldwave, overdriven-bass, gated-snare, 110 BPM, mono-low-end, no-scream
```

## Vocal anchor

- **Default:** Deep husky bass
- Альт. crooner-cold: Warm crooner (если нужен более «песенный» куплет)
- Альт. spoken bridge: Spoken word только на бридже

## Lyrics skeleton

```
[Intro]
[Structure: Minimalist Breakdown | Vinyl static | Synth Pad]

[Verse 1]
[Structure: Focused Performance]
[Whispered]
...

[Pre-Chorus]
[Structure: Build-up | Rolling Toms]
...

[Chorus]
[Structure: Anthemic Peak]
[Controlled Rock Vocal]
[Mid Register Only]
[No Scream]
...
(echo hook)

[Verse 2]
[Structure: Focused Performance]
...

[Bridge]
[Structure: Minimalist Breakdown | Rain | Silence]
...

[Chorus]
[Structure: Anthemic Peak | Sidechain pump]
...

[Outro]
[Structure: Outro Fade]
```

## Negatives

`no screaming, no shouting, no high-pitched vocals, no aggressive belting, no vocal acrobatics`

Дублировать в Style и перед припевом в Lyrics.

## Density / arrangement fix

Если режет инструменты в припеве, добавить в Style:
`non-stop rhythm section, constant bass groove, percussion stays active during chorus, full instrumental support behind vocals`

## Mix start (7-stem coldwave)

| Стем | дБ | Пан |
|---|---|---|
| anchor | -7 | C |
| bass | -5 | C |
| drums | -4 | C |
| vocal L/R | -2 | ±0.7 |
| synth L/R | -6 | ±0.85 |

Master bus pre: -3 dB · HS@12k+4 · HB@16k+2 · HP якоря ≤30 · моно-проверка обязательна.

## Master targets

- Mix: LUFS -20…-18 · crest >14 · peak <-3
- Master Spotify: LUFS -14 · crest 10–12 · peak -1.5…-2.0 · LRA 2–4

## Fail → fix

| Поломка | Фикс |
|---|---|
| Визг / ор | anti-scream блок + −5–10 BPM + Melodic/Classic rock framing |
| Пустой припев | non-stop rhythm section… |
| Каша 1–3k | vocal pocket: perfectly separated vocal pocket… |
| Убит бас после стемов | HP якоря ≤30 Гц; бас HP только 30 |
| Crest 3 (кирпич) | ослабить лимитер; цель crest 10–12 |

## Source

- Playbook: `genres/darksynth_coldwave.md`
- Synced from Notion 2026-07-11
