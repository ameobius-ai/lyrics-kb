# Suno-пакет: darksynth / coldwave

Зеркало Notion-страницы «Suno-пакет darksynth coldwave» (раздел «Плейбуки и Suno-пакеты»). Источник правды — там.

## Профиль

| Параметр | Значение |
|---|---|
| BPM | 105–115 (якорь **110**) |
| Тональность | Am / Em |
| Вокал | deep baritone, чуть подтоплен |
| Stem-философия | якорь-король |
| Платформа | Spotify −14 |
| Референсы | Molchat Doma, Boy Harsher, She Past Away |

## Style (вставить целиком)

```
[Vocal: male, deep husky timbre, relaxed but intense delivery, clear diction, precise rhythm, modern rap-adjacent tone], darksynth, coldwave, overdriven-bass, palm-mute-guitar, analog-arps, gated-snare, 110 BPM, intimate close-mic dry vocal combined with wide cold reverb wash, focused mono low-end, professional studio recording, no screaming, no shouting, no wailing, no humming, no vocal acrobatics
```

**Компакт (режь атмосферу, не вокал):**

```
[deep husky baritone], darksynth, coldwave, overdriven-bass, gated-snare, 110 BPM, mono-low-end, professional-studio-recording, no-scream
```

## Vocal anchors

- Default: Deep husky bass
- Альт. crooner-cold: Warm crooner (более «песенный» куплет)
- Альт. spoken bridge: Spoken word только на бридже

## Negatives

`no screaming, no shouting, no high-pitched vocals, no aggressive belting, no vocal acrobatics, no wailing, no humming, no ooh-ahh ad-libs, no vocals during intro`

## Плотность припева (если режет инструменты)

Добавить в Style: `non-stop rhythm section, constant bass groove, percussion stays active during chorus, full instrumental support behind vocals`

## 7-stem coldwave (старт)

| Стем | дБ | Пан |
|---|---|---|
| anchor | −7 | C |
| bass | −5 | C |
| drums | −4 | C |
| vocal L/R | −2 | ±0.7 |
| synth L/R | −6 | ±0.85 |

Master bus pre: −3 dB · HS @ 12k +4 · HB @ 16k +2.

## Master targets

Mix: LUFS −20…−18 · crest >14 · peak <−3
Master Spotify: LUFS −14 · crest 10–12 · peak −1.5…−2.0 · LRA 2–4

## EQ-стек на дефолтную Suno-генерацию (проверен на жанре)

```
low shelf −2.5 @ 100 Q0.7
high shelf +4 @ 3k Q0.7
high shelf +4 @ 10k Q0.7
limiter −0.5 dBTP
```

- low shelf 100 — снять гул/муть дефолтного низа
- +4 @ 3k — системный фикс thin_high (паттерн 3/3 тёмных кейсов подтверждён)
- +4 @ 10k — воздух
- Контекст: мастер поверх дефолтной генерации; при стем-миксе shelf @ 3k всё равно проверять на мастере

## Частые поломки → фикс

| Поломка | Фикс |
|---|---|
| Визг / ор | anti-scream блок + −5–10 BPM + Melodic/Classic rock framing |
| Завывания в интро | [No Vocals][No Humming][No Wailing][No Vocal Ad-Libs] в интро/INST + negatives |
| Пустой припев | non-stop rhythm section… |
| Каша 1–3k | vocal pocket: perfectly separated vocal pocket… |
| Убит бас после стемов | HP якоря ≤30 Гц; бас HP только 30 |
| Crest 3 (кирпич) | ослабить лимитер; цель crest 10–12 |