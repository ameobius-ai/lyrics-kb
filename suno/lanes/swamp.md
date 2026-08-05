# Suno-пакет: болотный фолк-электроник / dark slavic folk electronic

Зеркало Notion-страницы «Suno-пакет болотный фолк-электроник» (раздел «Плейбуки и Suno-пакеты»). Источник правды — там.

**Жанр строится на тишине.** Главный инструмент полосы — negative space: foley и паузы несут столько же смысла, сколько бит. Не заполняй пространство — Suno сам стремится залить всё звуком, держи его тегами `sparse`, `dry`, `negative space`.

## Профиль

| Параметр | Значение |
|---|---|
| BPM | 85–100 (якорь **95**), без half-time — рельеф делается плотностью |
| Тональность | D minor (вариант: A minor) |
| Вокал | male husky, dry close-mic, half-spoken куплеты · сдержанный низкий chant в припеве |
| Stem-философия | foley + sub критичны (это «гитары» жанра); бит вторичен |
| Микс-эстетика | blackened dry: близко, сухо, темно; mono low-end; без большого холла |
| Референсы | Shortparis, OLIGARKH, Theodor Bastard, IC3PEAK (тёмная сторона), trip-hop-грязь Massive Attack |

## Style (вставить целиком)

```
[Vocal: male, husky low register, dry close-mic, half-spoken verses, restrained low chant on chorus, whisper doubles, no vibrato], dark slavic folk electronic, industrial swamp blues, 95 BPM, D minor, deep sub drone, wet foley — water drips, reed rustle, mud squelch, sparse broken beat, dusty analog percussion, mono low-end, blackened dry mix, negative space, professional studio recording
```

**Компакт (режь атмосферу, не вокал и не foley):**

```
[male husky half-spoken, dry close-mic], dark slavic folk electronic, swamp blues, 95 BPM, D minor, sub drone, water-drip foley, sparse broken beat, blackened dry mix
```

## Vocal anchors

- Default куплет: half-spoken husky — рассказ хозяина территории, без нажима
- Припев: низкий chant + whisper double — формула зова, не гимн. Белтинг запрещён
- Точка: одиночный шёпот на последней строке секции

**Правило подачи:** вода не кричит. Любая строка громче mezzo — уже ошибка полосы. Эскалация делается плотностью фактуры, а не вокалом.

## Negatives

`pop, happy folk, flute solo, bright choir, polished pop mix, edm drop, trap hats, epic orchestra, big hall reverb, autotune, female vocals, opera vocals, four-on-the-floor, fade-out ending`

НЕ переноси металкор-негативы (`no lo-fi`, `no drum-machine feel`) — тут пыльная драм-машина и грязь легальны. И не добавляй `no screaming` из coldwave бездумно: лишние вокал-негативы схлопывают husky в эстрадный баритон.

## Master targets (болото ≠ метал!)

Mix: LUFS −20…−18 · crest >12 · peak <−6
Master: LUFS −12…−10 · crest 8–10 · true peak ≤ −1.0 dBTP · LRA 5–8

Полоса живёт динамикой и паузами: LUFS −9 её убьёт.

## EQ-стек на дефолтную Suno-генерацию (болотный профиль)

```
high-pass 25 Hz steep
bell +1.5 @ 55 Q1.0        (тело drone)
bell −3 @ 300 Q1.2         (короб, каша под вокалом)
bell +2 @ 2.5k Q1.4        (разборчивость husky-вокала)
high shelf −2 @ 10k Q0.7   (blackened: верх приглушён сознательно)
de-esser 5–7k
limiter −1.0 dBTP, цель crest 8–10
```

- Верх тут **режется**, а не добавляется — блеск = поломка
- Sub drone держать mono ниже 120 Гц

## Частые поломки → фикс

| Поломка | Фикс |
|---|---|
| Foley исчез | явные теги в интро/аутро + `wet foley` в Style; при провале — field recording поверх стема |
| Бит стал ровным хаусом | `sparse broken beat` • негатив `four-on-the-floor`; −5 BPM |
| Вокал уехал в эстрадный баритон | `husky, dry close-mic, half-spoken, no vibrato`; убрать лишние вокал-негативы |
| Появился эпик/оркестр | негативы `epic orchestra, bright choir`; убрать слова про cinematic |
| Sub гудит кашей | mono low-end, HP 25, сайдчейн drone от кика 1–1.5 дБ |
| Всё звенит/блестит | high shelf −2…−3 @ 10k; в Style усилить `blackened dry mix, dusty` |
| Suno заливает паузы ад-либами | `[No Vocals][No Humming]` в каждой инструментальной секции |