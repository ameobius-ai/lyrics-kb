# Энциклопедия — часть 4: оценка и машинные блоки (§28–30)

Зеркало Notion-страницы «encyclopedia». Master — там.

⚠️ **Важно:** здесь версия 1.0 (10 параметров). Актуальная — **Оценка 2.0** с 12 параметрами (+P11 пропеваемость, +P12 цельность), жанровыми весами, white-list и hard-fail — в Notion (master overlay E1 + Детектор 2.0). При конфликте overlay главнее.

## §28. Функция оценки (v1, историческая)

```
P1  concreteness      — конкретика vs абстракции
P2  rhythm_variance   — вариативность ритма vs ровность
P3  rhyme_quality     — неточные/ассонансные vs банальные/глагольные
P4  register_contrast — столкновение high/low vs один регистр
P5  body_code         — телесность vs романтизация
P6  ugly_aesthetics   — уродливое как персонаж vs абстрактный фон
P7  phonetics         — звукопись vs отсутствие
P8  hook_strength     — заедающий хук vs чеклист
P9  voice_embodiment  — тело/место/действие vs абстрактный «я»
P10 anti_ai_clean     — отсутствие AI-маркеров

score = sum(P1..P10), диапазон 0.0–10.0
```

**Вердикт:** ≥8.0 EXCELLENT · 7.0–7.9 GOOD · 5.0–6.9 SUSPECT · <5.0 SLOP. **Порог прохода: ≥ 7.0.**

### Цикл REPAIR

```
WHILE score < 7.0:
  1. Прогнать детектор → найти флаги
  2. Применить трансформации по флагам
  3. Оценить заново
  4. IF score не растёт 2 итерации → STOP, отдать с delta-отчётом
```

Максимум 3 итерации по версии 1.0. **Практика хаба:** REPAIR делается максимум один раз — второй круг выглаживает текст в среднее.

### Пример оценки (кейс «серверная»)

Слоуп-версия: P1=0.3, P2=0, P3=0.5, P4=0, P5=0, P6=0.2, P7=0, P8=0, P9=0.3, P10=0 → **1.3/10 SLOP**

После правки: P1=0.8, P2=0.7, P3=0.7, P4=0, P5=0, P6=0.2, P7=0, P8=1, P9=0.8, P10=0.7 → **4.9/10 SUSPECT**

Delta: P4 (регистровый контраст), P5/P6 (тело, уродливое), P7 (фонетика) → после REPAIR ~7.5.

## §29. Промпт-скаффолды

Четыре рабочих скаффолда (полные тексты — в Notion и в E2 «Усиление ремесла»):

- **GENERATE** — вход: бриф + вектор автора. Жёсткий блок ЗАПРЕЩЕНО (слова-маркеры, тех-метафоры, гипофора, «не X а Y», глагольные рифмы, припев-чеклист, объяснение позиции, одинаковая длина строк) + блок ОБЯЗАТЕЛЬНО (конкретика, один образ на строфу, удары а не слоги, enjambment, физический якорь). Выход: только текст с meta-tags.
- **AUDIT** — вход: текст. Выход: P1…P10 с одной фразой почему + score + verdict + delta.
- **REPAIR** — вход: текст + флаги. Таблица трансформаций: маркер-слово → конкретный образ · тех-метафора → телесное действие · чеклист → крюк · объяснение → действие · параллелизм без сдвига → градация.
- **CALIBRATE / BLEND** — сравнение с вектором автора / смешение двух векторов с проверкой совместимости (конфликты по density / meter / voice решаются в пользу одного).

## §30. Машинно-читаемые блоки

### Детектор: веса флагов

```json
{
  "tech_metaphor": 2.0,
  "chorus_checklist": 2.0,
  "truncation": 2.0,
  "organ_cliche": 1.5,
  "binary_light_dark": 1.5,
  "hypophora": 1.5,
  "not_x_but_y": 1.5,
  "position_explanation": 1.5,
  "marker_word": 1.0,
  "verb_rhyme": 1.0,
  "banal_rhyme": 1.0,
  "uniform_line_length": 1.0,
  "noun_stack": 0.5,
  "adj_pile": 0.5,
  "parallel_no_shift": 0.5
}
```

**Полосы AI-score:** 0–1.5 живое · 2–4 подозрение · 4.5+ слоуп. **Hard-fail:** любой флаг веса 2.0 → обязательный REPAIR независимо от суммы.

### Чек-лист «живое vs слоуп» (булев)

**Red flags** (все должны быть false): tech_metaphor_wrapping_emotion · chorus_is_checklist · explains_position · uniform_line_length · verb_rhymes · binary_light_dark_frame · hypophora · not_x_but_y · noun_stack_3plus · adj_pile_3plus · truncation · parallel_no_shift · banal_rhyme_pairs · marker_words · organ_cliches

**Green flags** (нужно ≥5): physical_anchor · register_contrast · refrain_anchor · concrete_noun · body_code_unromantic · ugly_as_character · internal_rhyme · enjambment · rhythm_variance · voice_embodied

**Pass condition:** все red == false И ≥5 green == true

### Дерево выбора голоса

```
рэп:
  быт/подворотня/панелька → marginal_at_bottom
  социальное наблюдение → witness_no_position
  литература/философия → intellectual_at_bottom
  нуар/город/история → narrator_noir
  поколение/исповедь → confessor
  абсурд/насилие → mask_of_absurd
пост-панк:
  апатия/быт → cold_declaimer
  тревога/страх → intellectual_at_bottom
поп-панк → mask_of_absurd
инди/неофолк → melancholic
spoken word → cold_declaimer
fallback → witness_no_position
```

### Расширение

Новый автор: строка в `pantheon` + вектор в `style_vectors` + ветка в `voice_decision_tree`.
Новый AI-маркер: запись в `detector` + вес в `weights` + правило трансформации.

---

## Финал

Энциклопедия — рабочий инструмент, не догма. Правила существуют, чтобы их нарушать — но осознанно.

**Один бьющий образ лучше трёх красивых, считай ритм вслух, и пусть философия живёт в подворотне.**