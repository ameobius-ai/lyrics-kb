# Suno-пакет: pre-cyberpunk analog (лейн)

Дочерний лейн darksynth/coldwave. Статус — лирика готова, аудио не рендерилось (pending_generation). Источник правды для чисел/слотов — `album.yaml` и `lint.yaml` альбома «ТРИ КОРОТКИХ» (не в этом репо; зеркало ниже — вытягивается конфигом, не наоборот).

Различие от родительского coldwave: аналоговая советская техника (телецентр, глушилка, лента, перфокарта, отк-приёмка, таксофон) вместо urban-decay-референсов; сквозный мотив — учёт/надзор (считают, вносят, подшили) как второй словарь наряду с бытом техники.

## Профиль

| Параметр | Значение |
|---|---|
| BPM | 92–116 по названным константам (slow/mid_slow/mid/mid_high/anchor/high/drive), якорь лейна — 108 |
| Тональность | A minor / E minor, чередуются потреково | 
| Вокал | male deep husky baritone — 7 вариантов манеры на лейн (half-spoken / chant / whisper-double / report / foreman / conversational / urgent) |
| Stem-философия | якорь-король (унаследовано из coldwave) |
| Платформа | Spotify −14 |
| Лексика | двусловарная: быт советской техники (перфокарта, глушилка, ОтК, таксофон) + учёт/надзор (считают, вносят, подшили) |

## Style (9 слотов, строго по порядку — канон style-tag-grammar.md)

Пример (PRE-001, якорный BPM 108):
```
[Vocal: male, deep husky baritone, half-spoken verses, dry close-mic, clear diction, restrained delivery], coldwave, darksynth, 108 BPM, A minor, mono sub-bass under slow analog drone, foley: tuning-dial static sweeps, TV snow hiss, foil rustle, brushed gated-snare over slow machine pulse, intimate dry vocal against wide cold reverb wash, professional studio recording
```

Второй пример (PRE-007, drive BPM 116, industrial-вариант):
```
[Vocal: male, deep husky baritone, urgent but restrained, dry close-mic, clear diction], coldwave, darksynth, 116 BPM, A minor, relay-driven octave bass, hard and dry, foley: relay switch clacks, PA test tone, ball bouncing off a wall, sequenced EBM sixteenths with industrial snare, bright hard-panned industrial mix with vocal pocket carved, professional studio recording
```

Foley (2–4 источника) — носитель индивидуальности трека, различается на каждом треке: тюнинг-диск / трансформатор / бобина / перфокарты / штамп / телефон / реле / накал лампы.

## Vocal anchors (7)

- `baritone_halfspoken` — дефолт куплета
- `baritone_chant` — присв
- `baritone_whisper_double` — двойной шёпот на повторе присва
- `baritone_report` — протокольная подача (ПЕРФОКАРТА)
- `baritone_foreman` — интонация мастера цеха (ОТК)
- `baritone_conversational` — бридж-разговор (ТАКСОФОН)
- `baritone_urgent` — тревога без срыва (ПРОФИЛАКТИКА)

## Negatives

`no screaming, no shouting, no high-pitched vocals, no aggressive belting, no vocal acrobatics, no wailing, no humming, no ooh-ahh ad-libs, no vocals during intro`

## Exclude: база coldwave + лейн-добавка

База (style-tag-grammar.md §6) + `warm analog pads`. Для industrial-фактурного трека (ПРОФИЛАКТИКА) добавляется `gore decor`.

## Дифференциация соседних треков

Минимум 2 слота из {tempo, low_end, foley, rhythm, mix} обязаны отличаться от соседа. Подтверждено на всех 7 переходах альбома «требуоткового генератора» `build.py` (1276 проверок, 0 ошибок) — tempo+low_end+foley+rhythm+mix различаются на каждой границе (все 5 из 5, а не минимум 2) — дифференциация системная, не точечная.

## Форма (канон 9 шагов, унаследован из coldwave)

Intro(short) → V1 → Pre-Chorus → Chorus → V2 (бит тоньше) → Pre-Chorus (обязательный сдвиг хотя бы одной строки) → Chorus ×2 → Bridge(short, вопрос+утверждение) → Outro(short, факт/кадр, без морали).

**Урок этого лейна:** если первая строка pre1/pre2 повторяется как якорь-крюк (легитимный приём), вторая строка обязана нести новый факт/направление, а не переставленные слова первой. Слабый повтор пойман и починен в PRE-003/PRE-004/PRE-008 на REPAIR (см. кейсы) — кандидат на паттерн-линт (см. issue «pre-chorus shift validator»).

## Master targets (унаследовано)

Mix: LUFS −20…−18 · crest >14 · peak <−3
Master Spotify: LUFS −14 · crest 10–12 · peak −1.5…−2.0 · LRA 2–4

## EQ-стек (унаследован, с одним лейн-исключением)

```
low shelf -2.5 @ 100 Q0.7
high shelf +4 @ 3k Q0.7
high shelf +4 @ 10k Q0.7
limiter -0.5 dBTP
```

Исключение: **ПРОФИЛАКТИКА (116 BPM, industrial-фактура)** — не применять +4 @ 3k до первой генерации; 2–5 кГц уже жёсткие на industrial-текстуре, патч из coldwave может задвоить presence. Гипотеза, 0 генераций — подтвердить по факту.

## Частые поломки → фикс (унаследовано + 1 новая)

| Поломка | Фикс |
|---|---|
| Визг / ор | anti-scream блок + −5–10 BPM + Melodic/Classic rock framing |
| Завывания в интро | [No Vocals][No Humming][No Wailing][No Vocal Ad-Libs] в интро/INST + negatives |
| Пустой припев | non-stop rhythm section, constant bass groove, percussion stays active during chorus, full instrumental support behind vocals |
| Каша 1–3k | vocal pocket: perfectly separated vocal pocket… |
| Убит бас после стемов | HP якоря ≤30 Гц; бас HP только 30 |
| Crest 3 (кирпич) | ослабить лимитер; цель crest 10–12 |
| Pre-chorus читается как повтор | вторая строка pre2 обязана менять факт/время/направление, не только слова первой |

## Связанное

- Конфиг-источник правды: `album.yaml`/`lint.yaml` альбома «ТРИ КОРОТКИХ» (PRE-001…008)
- Кейсы: `cases/PRE-001-*.md` … `cases/PRE-008-*.md`
- Родитель: `suno/lanes/coldwave.md`
