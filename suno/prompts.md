# Suno: промпт-инженерия

## Custom mode

Структура через meta-tags в лирике:
```
[Intro]
[Verse]
[Pre-Chorus]
[Chorus]
[Bridge]
[Drop]
[Build]
[Climax]
[Catchy Hook]
[Outro]
[Instrumental Break]
```

## Правила форматирования тегов (v5+)

**Квадратные скобки `[ ]` — структурные/технические теги, всегда на английском:**
- `[Intro]`, `[Verse]`, `[Chorus]`, `[Bridge]`, `[Build]`, `[Drop]`, `[Outro]` и т.д.
- Behavior tags: `[Structure: Anthemic Peak]`, `[Whispered]`, `[Ad-libs]` и т.д.
- Инструментальные переключения: `[Distorted Guitar]`, `[Synth Pad]`, `[Breakbeat]`
- Pipe-комбинации: `[Chorus | High Energy | Anthemic | Electric Guitar Solo]`
- Все технические теги — ТОЛЬКО в квадратных скобках, только английский

**Круглые скобки `( )` — подпевка / backing vocals ONLY:**
- Текст в круглых скобках воспринимается как бэк-вокал
- Пример: `ржавчина на пальцах (ржавчина)` → основная строка + эхо-подпевка
- **НЕ использовать для транскрипции/ромадзи**: `全ては私が (Subete wa watashi ga)` — ОШИБКА, Suno споёт и то и другое как две строки
- Транскрипция идёт ОТДЕЛЬНО от лирики, не в скобках внутри Lyrics box
- Скобки = только слова которые должны звучать как подпевка

**Style поле — только жанр/настроение/инструменты/вокал:**
- Никаких структурных тегов в Style
- Никаких `[Verse]`, `[Drop]`, `[Build]` в Style — они живут в Lyrics
- Style: `darksynth, coldwave, overdriven bass, deep baritone, 110 BPM`
- Vocal anchors: `[Vocal: male, deep husky timbre...]` — допустимо в Style

[добавлено: практика + Discord Producers, 2026-07-02]

## Style tags

Категории что работают:
- жанр (house, techno, dnb, folk, synthwave...)
- настроение (melancholic, uplifting, dark...)
- инструменты (analog synth, acoustic guitar, 808...)
- вокальный стиль (warm male vocal, ethereal female...)
- эпоха (80s, 90s, modern...)
- продакшен-характеристики (lo-fi, polished, raw, bedroom...)

**Что Suno игнорирует:** слишком специфичные технические термины, внутренние DAW-команды.

**Что Suno усиливает:** жанровые якоря, вокальные дескрипторы, эмоциональные слова.

**Негативные описания:** через `no screaming`, `no shouting` — работают когда продублированы и в style и в лирике.

## Persona

- Создание голоса через референс-аудио
- Тренировка характера вокала
- Один persona = один характер

## Extensions

- Продлить / обрезать / достать стемы
- Когда лучше регенерировать: если структура ломается
- Когда лучше экстендить: если звук хорош но не хватает длины

## Cover mode

- Применяет новый стиль к существующему аудио
- Ограничения по длине

## Audio upload / style reference

- Загрузка референс-аудио для стиля
- Подводные: Suno может перебрать и потерять характер оригинала

[источник: практика]
