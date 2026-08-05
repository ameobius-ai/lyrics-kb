# Жанр → BPM карта (420 жанров, 865 артистов)

Источник: SiliconSense catalog (865 артистов). Реальные данные, не догадки.
Для каждого жанра: количество артистов, средний BPM, диапазон.
Заменяет хардкод-догадки в генераторе стиля.

## Топ-30 жанров (по количеству артистов)

| жанр | артистов | avg BPM | диапазон |
|---|---|---|---|
| russian-pop | 37 | 118 | 98–132 |
| dance-pop | 26 | 115 | 98–132 |
| synth-pop | 19 | 120 | 102–145 |
| pop-rock | 17 | 123 | 95–150 |
| eurodance | 15 | 133 | 122–142 |
| russian-estrada | 15 | 110 | 78–125 |
| pop-rap | 15 | 107 | 85–140 |
| russian-chanson | 12 | 95 | 75–122 |
| k-pop | 11 | 123 | 100–138 |
| estrada | 9 | 112 | 92–122 |
| post-punk | 9 | 127 | 110–145 |
| contemporary-rnb | 7 | 98 | 72–138 |
| eurodisco | 7 | 122 | 118–125 |
| chanson | 7 | 92 | 72–115 |
| hard-rock | 6 | 116 | 90–140 |
| alternative-rock | 6 | 108 | 95–130 |
| vocal-jazz | 6 | 91 | 58–120 |
| arena-rock | 6 | 114 | 98–130 |
| russian-bard | 6 | 95 | 90–105 |
| boom-bap | 6 | 91 | 89–95 |
| soviet-via | 6 | 101 | 82–118 |
| sophisti-pop | 5 | 112 | 100–120 |
| soft-rock | 5 | 87 | 75–118 |
| russian-rock | 5 | 107 | 98–120 |
| indie-rock | 5 | 142 | 130–158 |
| ethno-pop | 5 | 116 | 105–130 |
| teen-pop | 5 | 111 | 100–120 |
| art-pop | 5 | 102 | 85–120 |
| new-wave | 5 | 114 | 92–132 |
| brazilian-phonk | 5 | 144 | 140–145 |

## Полная карта (машинно-читаемый JSON)

```json
{"russian-pop":{"count":37,"avg":118,"min":98,"max":132},"dance-pop":{"count":26,"avg":115,"min":98,"max":132},"synth-pop":{"count":19,"avg":120,"min":102,"max":145},"pop-rock":{"count":17,"avg":123,"min":95,"max":150},"eurodance":{"count":15,"avg":133,"min":122,"max":142},"russian-estrada":{"count":15,"avg":110,"min":78,"max":125},"pop-rap":{"count":15,"avg":107,"min":85,"max":140},"russian-chanson":{"count":12,"avg":95,"min":75,"max":122},"k-pop":{"count":11,"avg":123,"min":100,"max":138},"estrada":{"count":9,"avg":112,"min":92,"max":122},"post-punk":{"count":9,"avg":127,"min":110,"max":145},"contemporary-rnb":{"count":7,"avg":98,"min":72,"max":138},"eurodisco":{"count":7,"avg":122,"min":118,"max":125},"chanson":{"count":7,"avg":92,"min":72,"max":115},"hard-rock":{"count":6,"avg":116,"min":90,"max":140},"alternative-rock":{"count":6,"avg":108,"min":95,"max":130},"vocal-jazz":{"count":6,"avg":91,"min":58,"max":120},"arena-rock":{"count":6,"avg":114,"min":98,"max":130},"russian-bard":{"count":6,"avg":95,"min":90,"max":105},"boom-bap":{"count":6,"avg":91,"min":89,"max":95},"soviet-via":{"count":6,"avg":101,"min":82,"max":118},"sophisti-pop":{"count":5,"avg":112,"min":100,"max":120},"soft-rock":{"count":5,"avg":87,"min":75,"max":118},"russian-rock":{"count":5,"avg":107,"min":98,"max":120},"indie-rock":{"count":5,"avg":142,"min":130,"max":158},"ethno-pop":{"count":5,"avg":116,"min":105,"max":130},"teen-pop":{"count":5,"avg":111,"min":100,"max":120},"art-pop":{"count":5,"avg":102,"min":85,"max":120},"new-wave":{"count":5,"avg":114,"min":92,"max":132},"brazilian-phonk":{"count":5,"avg":144,"min":140,"max":145},"acoustic-pop":{"count":5,"avg":104,"min":92,"max":115},"electro-pop":{"count":5,"avg":127,"min":120,"max":130},"europop":{"count":4,"avg":119,"min":108,"max":128},"synth-rock":{"count":4,"avg":127,"min":115,"max":145},"folk-rock":{"count":4,"avg":99,"min":90,"max":105},"progressive-house":{"count":4,"avg":127,"min":126,"max":128},"grunge":{"count":4,"avg":103,"min":92,"max":125},"classic-soul":{"count":4,"avg":92,"min":72,"max":120},"reggaeton":{"count":4,"avg":98,"min":95,"max":102},"big-band-swing":{"count":4,"avg":148,"min":120,"max":190},"traditional-pop":{"count":4,"avg":94,"min":80,"max":105},"roots-reggae":{"count":4,"avg":80,"min":75,"max":92},"glam-metal":{"count":4,"avg":118,"min":102,"max":130},"rockabilly":{"count":4,"avg":152,"min":135,"max":168},"russian-dance-pop":{"count":4,"avg":125,"min":120,"max":128},"progressive-rock":{"count":4,"avg":112,"min":85,"max":128},"vaporwave":{"count":3,"avg":72,"min":68,"max":80},"classic-female-blues":{"count":3,"avg":79,"min":72,"max":92},"neo-soul":{"count":3,"avg":94,"min":78,"max":112},"art-rock":{"count":3,"avg":114,"min":105,"max":125}}
```

## Заметки

- **russian-pop** (37 артистов) — самый представленный жанр, 118 BPM avg. окно 98–132
- **eurodance** стабильно быстрый — 133 avg, узкий разброс 122–142
- **boom-bap** максимально плотный — 91 avg, разброс всего 89–95
- **indie-rock** наоборот — 142 avg, широкий 130–158
- **vaporwave** самый медленный — 72 avg
- **big-band-swing** самый быстрый — 148 avg, разброс до 190
- **rockabilly** — 152 avg, всегда быстрый

## Распределение по декадам

| декада | артистов |
|---|---|
| 1990s | 208 |
| 2010s | 193 |
| 2000s | 117 |
| 1980s | 111 |
| 1970s | 69 |
| 2020s | 47 |
| 1960s | 34 |
| 1950s | 23 |
| 1930s | 22 |
| 1940s | 21 |
| 1920s | 20 |

## Источник

865 артистов из SiliconSense catalog. BPM указан как диапазон (например "75–170"),
значения усреднены. Полный JSON (все 420 жанров) — в исходном дампе
`catalog_artists_complete.json`.
