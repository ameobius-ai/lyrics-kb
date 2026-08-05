# Suno-пакет: metalcore / post-hardcore

Зеркало Notion-страницы «Suno-пакет metalcore post-hardcore» (раздел «Плейбуки и Suno-пакеты»). Источник правды — там.

**Две полосы в одном пакете.** Metalcore — агрессия, чугунный брейкдаун, скрим-ведущий. Post-hardcore — динамика тихо/громко, чистый тенор ведёт, скрим как удар. Не смешивай Style-блоки: выбери полосу, потом добавляй элементы второй точечно.

## Профиль

| Параметр | metalcore | post-hardcore |
|---|---|---|
| BPM | 150–175 (якорь **160**) | 135–155 (якорь **145**) |
| Half-time брейкдаун | ~80 | ~72 |
| Тональность | Em / drop-D, drop-C# | Dm / Bm, open drop-D |
| Вокал | harsh mid-scream + gang shouts | clean tenor ведёт, scream бьёт |
| Stem-философия | стемы-заменяют (гитарная стена) | гитарная пара-король |
| Платформа | Spotify −14 | Spotify −14 |
| Референсы | Architects, While She Sleeps, Bury Tomorrow, Spiritbox, Ice Nine Kills | Underoath, Silverstein, Holding Absence, Boston Manor, La Dispute |

## Style — metalcore (вставить целиком)

```
[Vocal: male, harsh mid-range scream, aggressive but fully intelligible enunciation, gang-shout layers on hook, controlled clean belt only on chorus lift], metalcore, modern-hardcore, drop-D-riffing, palm-muted-chugs, double-kick-drive, half-time-breakdown at 80 BPM, soaring-octave-lead, 160 BPM, tight-gated-drums, quad-tracked-hard-panned-guitars, punishing-mono-low-end, professional studio production, no guttural death growl, no autotune, no pop-clean-vocals, no lo-fi
```

**Компакт:**

```
[harsh mid-scream + gang shouts], metalcore, drop-D chugs, double-kick, half-time-breakdown-80, 160 BPM, quad-tracked-guitars, no-autotune, no-growl
```

## Style — post-hardcore (вставить целиком)

```
[Vocal: male, dual delivery — raw emotive clean tenor on choruses, throat-shred scream on verses, cracked sincerity, clear diction], post-hardcore, melodic-hardcore, octave-chord-shimmer, driving-eighth-note-bass, dynamic loud-quiet-loud arrangement, anthemic gang-vocal bridge, 145 BPM, roomy-live-drums, wide-stereo-guitars, warm-analog-saturation, professional studio production, no autotune, no trap hats, no synth-pop gloss, no death growl
```

**Компакт:**

```
[clean tenor + scream duet], post-hardcore, melodic-hardcore, octave-shimmer, loud-quiet-loud, 145 BPM, live-room-drums, no-autotune, no-gloss
```

## Vocal anchors

- Default metalcore: harsh mid-scream — самый разборчивый регистр
- Hook: gang shout — 4–8 голосов в унисон, только 1–2 строки припева
- Breakdown: guttural low — короткая точка, 2–4 слова
- Default post-hardcore: cracked clean tenor — на грани срыва
- Контраст: scream/clean duet — скрим-строка и чистая строка подряд, не одновременно

**Правило регистра:** один слой — одна задача. Скрим и чистый в одном теге = каша или поп-вокал.

## Про инструментальный лид / соло

**Дефолт — без отдельного соло.** Лид-момент живёт в октавном лиде над припевом. Добавляй `[Lead Break]` осознанно: пост-хардкорная полоса, профиль Spiritbox/Ice Nine Kills, трек длиннее ~3:40, инструментал. Вредит: между брейкдауном и финальным припевом; в злом памфлетном тексте (кейс TOXIC — сознательно без соло); как замена бриджа. Максимум 8 тактов + `[No Vocals][No Humming]`.

## Negatives (инвертированы относительно coldwave!)

`no autotune, no pop-clean-vocals, no synth-pop gloss, no trap hats, no lo-fi, no guttural death growl on verses, no unintelligible screaming, no thin guitars, no drum-machine feel, no fade-out chorus`

НЕ копируй coldwave-негативы (`no screaming, no shouting, no belting`) — они убивают жанр. Самая частая ошибка переноса пакета.

## Мощь припева (если проседает)

Добавить в Style: `chorus lifts an octave, doubled rhythm guitars, gang vocals under lead line, ride cymbal opens, bass follows root — full wall behind vocal, no instrumental drop-out`

## 7-stem metalcore (старт)

| Стем | дБ | Пан |
|---|---|---|
| rhythm gtr L/R | −6 | ±1.0 |
| lead gtr | −9 | ±0.5 |
| bass | −5 | C |
| kick | −4 | C |
| snare / overheads | −4 | C / ±0.6 |
| vocal main | −3 | C |
| gang / backs | −9 | ±0.8 |

Master bus pre: −3 dB · HP @ 35 · bell −3 @ 300.

## Master targets

Mix: LUFS −18…−16 · crest >10 · peak <−3
Master (жанровый): LUFS −9…−7 · crest **6–8** · true peak ≤ −1.0 dBTP · LRA 3–5

**Метал ≠ coldwave.** −14 звучит вяло, но crest <5 — уже кирпич (over_master). Кейс: TOXIC вышел LUFS −8.1 / crest 3.9 / TP +1.0 — громкость ок, динамика и запас убиты.

## EQ-стек на дефолтную Suno-генерацию (метал-профиль)

```
high-pass 35 Hz steep
bell +2 @ 80 Q0.9        (панч бочки)
bell −3 @ 300 Q1.2       (короб / муть)
bell −2.5 @ 2.5k Q1.5    (физz медиатора, визг тарелок)
high shelf +3 @ 8k Q0.7  (воздух без песка)
limiter −1.0 dBTP, цель crest 6–8
```

- Метал-муть живёт в 250–400, а не в 100 — не срезай низ шельфом как в coldwave
- 2.5k у Suno-метала регулярно перегружен: пик медиатора + скрим + краш в одной полосе

## Частые поломки → фикс

| Поломка | Фикс |
|---|---|
| Брейкдаун не случился | явный тег `[Heavy Breakdown]` • `[Half-time 80 BPM]` • дублировать в Style |
| Скрим неразборчив | `intelligible enunciation` • `mid-range scream, not guttural` • −10 BPM |
| Дэткор-гроул вместо металкора | `no guttural death growl` в Style и Negatives; гроул только в теге брейкдауна |
| Чистый припев уехал в поп-балладу | `raw belt, cracked edge, no autotune, no pop-gloss` • gang-слой под лидом |
| Гитары тонкие | `quad-tracked hard-panned rhythm guitars, tight low-mid body` • bell +2 @ 200 на стеме |
| Бочка съедает бас | сайдчейн баса от кика 1.5 дБ, 30 мс; HP баса 30 Гц |
| Crest <5 (кирпич) | ослабить лимитер, вернуть транзиент снейра; цель 6–8 |
| Gang-вокал как хор-мультик | 2–4 дубля, ±0.8, срезать выше 6k, только 1–2 строки |