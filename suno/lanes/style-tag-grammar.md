# Грамматика Style-промптов и behavior-тегов — канон всех лейнов

Зеркало Notion-страницы «Грамматика Style-промптов и behavior-тегов — канон всех лейнов» (раздел «Плейбуки и Suno-пакеты»). Источник правды — там.

Style-промпт и behavior-теги — часть сонграйтинга, а не продакшна: они задают вокальную режиссуру и архитектуру формы.

## 1. Порядок слотов Style (9 слотов, строго по порядку)

1. vocal-блок `[Vocal: …]`
2. жанровая пара
3. BPM
4. тональность
5. низ / дрон
6. **foley** (2–4 источника) — носитель индивидуальности трека
7. ритм / перкуссия
8. характер микса
9. `professional studio recording`

## 2. Правило саунд-дифференциации

Соседние треки одного лейна обязаны различаться **минимум в 2 слотах из {3, 5, 6, 7, 8}**. Введено после copy-paste Style у CW-006…008 (три трека слились по звуку). В карточке трека фиксируется блоком «🎯 Дифференциация». Ядро лейна неприкосновенно (жанровая пара, mono low-end, вокальный канон, professional studio recording, анти-вейл).

## 3. Словарь behavior-тегов (3 класса)

**А. Вокальная манера:** `[half-spoken, husky, dry close-mic]` · `[low chant, restrained]` · `[whisper, dry]` · `[low unison whisper-choir doubles]` · `[call-response]`

**Б. Вход / выход слоёв — правило «одно событие на секцию»** (два и больше Suno игнорирует): `[drone swells]` · `[broken beat enters]` · `[beat thins out]` · `[whisper double joins]` · `[sub dies last]`

**В. Структурные директивы:** `[Structure: …]` · `[No Vocals][No Humming]` (без No Humming даёт Mm-вокализ) · `(short)` · `[End]`

## 4. Структурный канон текста (9 шагов)

Intro(short) → V1 → Pre-Chorus → Chorus → V2 (бит тоньше) → Pre-Chorus (сдвиг строки) → Chorus (только ×2) → Bridge(short, двухфазный) → Outro(short) + шёпот-сид следующего трека.

## 5. Жёсткие запреты

1. Таймстемпы в тегах ([0:45]) — ломают структуру целиком
2. Mm-интро — интро только сюжетное
3. Проза и предложения в Style — парсится как шум, только тег-формат
4. Третий прогон припева
5. Одинаковый Style у соседних треков лейна
6. Latinate-регистр на быстром темпе (многосложные не проорутся)

## 6. Exclude: база + лейн-добавки

База: `happy folk, bright choir, epic choir, gospel choir, polished pop mix, edm drop, trap hats, epic orchestra, big hall reverb, autotune, opera vocals, four-on-the-floor, fade-out ending`

- фолк: + `flute solo`
- coldwave: + `warm analog pads`
- industrial: + `gore decor`

## 7. Связанное

- Уроки серии CW: `cases/CW-*.md` + канон-страница в Notion
- Анти-паттерны лирики: канон-страница в Notion (чек-лист до аудита)