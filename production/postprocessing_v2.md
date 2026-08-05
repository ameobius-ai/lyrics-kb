# ПОСТОБРАБОТКА AI-ГЕНЕРАЦИИ v2 (июнь 2026)

> обновление гайда от 29 мая. стек ушёл далеко: AudioSR → FlashSR, UVR → BS-Roformer, + MIDI

## проблема

Suno и ElevenLabs выдают 128kbps MP3 с срезом на 16kHz. транзиенты сглажены, верхние гармоники убиты, стерео плоское. это не лоу-фай — это сжатие. лечится.

---

## Этап 1: Восстановление верхних частот

**SOTA: FlashSR** (январь 2025, KAIST)
- one-step diffusion distillation — один проход вместо 200 шагов как у AudioSR
- resurrect'ит 16-20kHz: воздух в вокале, остриё транзиентов, HF-текстуры
- 48kHz output, mono. ~6GB VRAM
- модель: `laion/FlashSR_One-step_Versatile_Audio_Super-resolution` (3 файла: student_ldm 986MB, sr_vocoder 599MB, vae 1.6GB)

```bash
python enhance.py --input input.mp3 --output enhanced.wav
```

**проверка:** Audacity → Analyze → Plot Spectrum. сигнал после 16kHz = успех

**когда пропускать:** lo-fi, ambient, intentionally degraded треки

**старый AudioSR** всё ещё работает, но FlashSR в ~50x быстрее и качество не хуже

---

## Этап 2: Стем-сепарация

**SOTA: BS-Roformer** (MVSep/MSST framework). Demucs — unmaintained с 2024

### модель по задаче:

| модель | стемов | SDR | VRAM | когда |
|---|---|---|---|---|
| **PolarFormer** | vocals + instrumental | 11.00 | <2GB | лучший вокальный экстрактор |
| **htdemucs_6s** | drums, bass, other, vocals, guitar, piano | ~8.5 | <2GB | быстрый общий сплит |
| **mega53** | 53 инструмента | varies | >4GB/CPU | индивидуальные дорожки |

mega53 даёт: kick, snare, hh, toms, bass, synth, guitar (acoustic/electric), piano, brass, strings, sax, flute, violin, cello, organ, harmonica, lead-vocal, back-vocal — отдельно

```bash
# наш скрипт
python stem_splitter.py input.wav -m polarformer -o /tmp/stems
python stem_splitter.py input.wav -m htdemucs_6s -o /tmp/stems
python stem_splitter.py input.wav -m mega53 -o /tmp/stems --cpu
```

### зачем разделять

бас и SFX требуют противоположной обработки. басу — саб и компрессия. SFX — transient shaping и экайтинг. вместе нельзя — усилишь одно, сломаешь другое

PolarFormer разделяет на «музыкальное» и «немузыкальное» — для электронной музыки это ровно то что нужно

**когда пропускать:** минималистичный трек (бас + один SFX) — проще на мастер-шине

---

## Этап 3: MIDI-экспорт (новое)

**basic-pitch** (Spotify, open source)

извлекает MIDI из любого стема. загружаешь в DAW — транспонируешь, переписываешь под другой инструмент, перестраиваешь аранжировку

```bash
python stem_splitter.py input.wav -m htdemucs_6s -o /tmp/stems --midi
```

MIDI извлекается из: piano, other, guitar, bass (настраивается). вокал и барабаны — обычно бессмысленно

**когда нужно:** хочешь взять мелодию из AI-трека и переписать под свой синт. или транспонировать баслайн в другую тональность

---

## Этап 4: Мастеринг

после сепарации и обработки стемов — сборка и финальный полировочный проход

**таргеты по платформам:**
- Spotify: -14 LUFS, true peak -1 dB
- Apple Music: -16 LUFS
- YouTube: -14 LUFS

**инструменты:** любой лимитер (Pro-L, limiter No.6). multiband если есть муть. не пережимай — стриминг всё равно нормализует

---

## пайплайн одной командой

```bash
# полный цикл: апскейл → 6 стемов → MIDI
python enhance.py --input suno_output.mp3 --output enhanced.wav
python stem_splitter.py enhanced.wav -m htdemucs_6s -o /tmp/stems --midi
```

для вокала отдельно (если нужен чистый аcapella для ремикса):
```bash
python stem_splitter.py enhanced.wav -m polarformer -o /tmp/vocals
```

---

## что устарело с прошлого гайда

| было | стало | почему |
|---|---|---|
| AudioSR (200 шагов диффузии) | FlashSR (1 шаг) | distillation, ~50x быстрее |
| UVR 5/6 GUI | BS-Roformer CLI (MSST) | SDR выше, без GUI, скриптуется |
| MDX-Net 23 | BS-Roformer / PolarFormer | SDR 11.00 vs 10.17 |
| — | MIDI экспорт (basic-pitch) | нового не было |
| Demucs htdemucs | Demucs (unmaintained) → BS-Roformer | Meta бросила Demucs |
