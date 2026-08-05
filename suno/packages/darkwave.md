# Suno Package: Darkwave

Готовый релизный пакет. Копировать в Style / Lyrics. Не путать с darksynth (метал/хоррор-агрессия) и coldwave (минимал, Molchat Doma).

[источник: bitwize genres/darkwave + practice, 2026-07-19]

---

## Profile

| Параметр | Значение |
|---|---|
| BPM | 110–130 (якорь **120**) |
| Тональность (типично) | Am / Em / Dm |
| Вокал | baritone / deep detached, reverb+delay |
| Stem-философия | вокал + бас-линия + arps |
| Платформа default | Spotify -14 |
| Референсы | She Past Away, Lebanon Hanover, Boy Harsher, Drab Majesty, Twin Tribes, Clan of Xymox |

## Style

```
[Vocal: male baritone, deep detached delivery, reverb-drenched, cool mournful tone, precise diction], darkwave, cold synthesizers, analog-arps, drum-machine, pulsing bass, cavernous reverb, gated drums, 120 BPM, nocturnal melancholic, post-punk electronic, no screaming, no trap hi-hats, no bright pop
```

## Style compact

```
[deep baritone], darkwave, analog-arps, drum-machine, pulsing-bass, 120 BPM, cavernous-reverb, no-scream
```

## Vocal anchor

- **Default:** Deep detached baritone
- Альт. female: cool detached alto, reverb wash
- Альт. spoken bridge: deadpan spoken only on bridge

## Lyrics skeleton

```
[Intro]
[Structure: Minimalist Breakdown | Analog Pad | Drum Machine Tick]

[Verse 1]
[Structure: Focused Performance]
[Detached]
...

[Pre-Chorus]
[Structure: Build-up | Sequencer Rise]
...

[Chorus]
[Structure: Anthemic Peak]
[Controlled Delivery]
[Mid Register Only]
...
(echo hook)

[Verse 2]
[Structure: Focused Performance]
...

[Bridge]
[Structure: Minimalist Breakdown | Silence | Pad]
...

[Chorus]
[Structure: Anthemic Peak]
...

[Outro]
[Structure: Outro Fade | Sequencer Decay]
```

## Negatives

`no screaming, no shouting, no trap hi-hats, no bright pop, no cheerful tone, no metal guitars, no hyperpop glitch vocals`

## Density / arrangement fix

Если припев пустой:
`constant bass pulse, drum machine stays active during chorus, arpeggio support behind vocals`

## Mix start (stems)

| Стем | дБ | Пан |
|---|---|---|
| vocal | -2 | C |
| bass | -5 | C |
| drums | -4 | C |
| arps L/R | -6 | ±0.7 |
| pads | -8 | wide |

Master bus: mono low-end <200Hz · HS@10k +2 if dead · Spotify -14 · crest 10–12

## Fail → fix

| Поломка | Фикс |
|---|---|
| Слишком «синфвейв-ностальгия» | убрать outrun/neon; add cold / post-punk / detached |
| Вокал кричит | anti-scream + Mid Register Only + −5 BPM |
| Пустой припев | constant bass pulse… |
| Каша 1–3k | cut arps −2dB @ 2k; vocal pocket |

## Source

- bitwize: `genres/darkwave`
- Related packages: `darksynth_coldwave.md` (холоднее/минимальнее), not pure metal-darksynth
