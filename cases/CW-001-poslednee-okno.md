# CW-001 — ПОСЛЕДНЕЕ ОКНО

- **Лейн:** darksynth / coldwave · **BPM:** 110 · **Вокал:** deep husky bass
- **Score лирики:** 8.1 EXCELLENT
- **Статус:** CLOSED (калибровочный трек серии)

## Значение кейса

Калибровочный трек серии: на нём выставлены плейбук, вокальный якорь и мастер-таргеты для всей CW-спины. Пакет CW-001 объявлен эталоном: все последующие Style/Negatives серии — его производные. Эталонный комплект: Style (полный + компакт), Vocal anchor, Lyrics box с behavior-тегами, Negatives.

## Метрики (факт)

| Метрика | Значение |
|---|---|
| LUFS out | −12.5 |
| True peak | −0.2 |
| Crest | 14.4 |
| chosen_gen | winner: suno_cover, gen_count 3 |

**fail_mode:** thin_low

**Лечение (ушло в урок серии):** thin_low/thin_high лечится в мастеринге: low shelf −2 @ 100 · high shelf +2.5 @ 3k · +3 @ 10k · limiter −1.0 TP. Позже выросло в стандартный EQ-стек серии: low shelf −2.5 @100 Q0.7 · high shelf +4 @3k · +4 @10k · limiter −0.5 dBTP.

## Уроки

1. Схема инструменталов серии: INST-solo после 1-го припева, bridge тихий сам по себе — без decay-вставки.
2. Пайплайн treblo inspo → suno_cover подтверждён как рабочий.
3. Спина серии: CW spine 6/6 closed — canon freeze gate достигнут на этом фундаменте.

## Примечание

В старом репо кейс лежал как `cases/CW-001-poslednee-okno.md` (pipeline/packages/CW-001, бриф для Hermes). Здесь восстановлен по канон-фактам из Notion.