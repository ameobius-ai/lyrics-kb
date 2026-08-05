# Radar: music-gen инструменты — 2026-08-04

> Решения за день. Локальная генерация песен ЛО отклонил полностью:
> «нам не нужен ни ACE-Step ни HeartMuLa», «локальную генерацию песен
> вообще убирай — излишняя нагрузка на инфру. достаточно облачной».

## Вердикты

| Проект | ★ | Вердикт | Почему |
|---|---|---|---|
| timoncool/ACE-Step-Studio | 301 | **NO-SHIP** | ACE-Step — «хуйня для лохов» (ЛО) |
| 0xShug0/audio.cpp | ~1k | **REFERENCE** | ценный из-за HeartMuLa/ACE-Step — не актуально; TTS у нас свой |
| timoncool/ACE-Step-Studio-pinokio | 13 | NO-SHIP | семейство ACE-Step |
| SamurAIGPT/Generative-Media-Skills | 3970 | **REFERENCE** | платный агрегатор muapi.ai (Suno/Veo3/Kling…); у нас работают chirp/FreeTheAi + DashScope + MOSS — платная дубль-зависимость не нужна |
| AceDataCloud/SunoMCP | 38 | **REFERENCE** | MCP-обёртка Suno; у нас chirp_generate уже встроен |
| calesthio/Resonant | 51 | REFERENCE | локальная студия Windows, вне стека |
| Anil-matcha/suno-comfyui | 20 | REFERENCE | ComfyUI-ноды Suno, ниша |
| bitwize-music-studio/claude-ai-music-skills | 399 | **INGESTED** | v5-best-practices слит: suno/bitwize_v5_practices.md |

## Рабочий стек после решения
- Генерация песен: **только облако** — chirp_generate (FreeTheAi v5-5), Suno
- Продакшен: openDAW/sota (stem split, анализ, микс)
- SFX: MOSS-SoundEffect; TTS: EN Soprano / RU Gemini
- Изображения: DashScope (wan2.7 / qwen-image / z-image)

## Ссылки
- [ACE-Step-Studio](https://github.com/timoncool/ACE-Step-Studio)
- [audio.cpp](https://github.com/0xShug0/audio.cpp)
- [Generative-Media-Skills](https://github.com/SamurAIGPT/Generative-Media-Skills)
- [SunoMCP](https://github.com/AceDataCloud/SunoMCP)
