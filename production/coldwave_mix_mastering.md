# Coldwave/darksynth 7-stem mix → mastering

## Жанровый профиль
- **BPM:** 110 (NOT 130/metal)
- **Key:** Am
- **Vocal:** deep baritone, чуть подтоплен в миксе (user preference)
- **Character:** overdriven bass + palm-mute + analog arps + gated snare
- **References:** Molchat Doma, Boy Harsher, She Past Away

## Stage 1: Stem setup (7 stems)

Стемы из Suno (cover как anchor + отдельные стемы из Advanced Split):

| # | Stem | Source | Start level | Pan |
|---|------|--------|-------------|-----|
| 1 | anchor | Cover (full track) | -7 dB | center |
| 2 | bass | bass_0 | -5 dB | center |
| 3 | drums | drums_1 | -4 dB | center |
| 4 | vocal_L | Lead Vocal | -2 dB | -0.7 |
| 5 | vocal_R | Lead Vocal(1) | -2 dB | +0.7 |
| 6 | synth_L | Synth | -6 dB | -0.85 |
| 7 | synth_R | Synth(1) | -6 dB | +0.85 |

**Master bus:** output -3 dB + HS@12k+4 + HB@16k+2

**Pan в openDAW:** `auBox.panning.setValue(-1.0..+1.0)` — NOT trackBox.pan. 0=center.

## Stage 2: Mix iteration (single-variable)

**ПРИНЦИП: одно изменение за итерацию.** Render → measure → suggest next → repeat.

### Что worked:
1. **Level balancing** — bass -3, minus -2, vocal +1, vocals_pf +1. По одному
2. **Кавер как anchor** — Cover вместо оригинала + стерео-вокал ±0.7, синты ±0.85. Дало лучший gap
3. **HS@12k +8** (вместо +4) — воздух удвоился 0.29→0.54. Чистое усиление без побочек
4. **Pedalboard bass saturation** — в коде, НЕ openDAW waveshaper. Саб 48→46, gap→0, воздух +0.12
5. **Mastering** — лимитер +6.4 LU, потолок -2.0 dBTP. LUFS -20.6→-14.2. Spotify PASS

### Что НЕ работает в openDAW (offline render):
- **Waveshaper** (hardclip) — ноль изменений (15% → 35% mix). Игнорируется при офлайн-рендере
- **Tidal** — тишина
- **Waveshaper + Compressor вместе** — graph error
- **DattorroReverb** на вокале — РАБОТАЕТ (единственный эффект что работает)

**Workaround:** openDAW effects (кроме gain/pan/EQ/DattorroReverb) ненадёжны в офлайне. Используй pedalboard в Python.

## Stage 3: Pedalboard processing

### Bass saturation (вместо waveshaper):
```python
from pedalboard import Pedalboard, LowShelfFilter, HighShelfFilter
import soundfile as sf
y, sr = sf.read('input.wav')
board = Pedalboard([
    LowShelfFilter(cutoff_frequency_hz=200, gain_db=-1),
    HighShelfFilter(cutoff_frequency_hz=12000, gain_db=+4),
])
y_out = board.process(y, sr)
sf.write('output.wav', y_out, sr)
```

### Mastering (limiter):
```python
from pedalboard import Limiter, Gain
# F12 settings: +6.4 LU gain, ceiling -2.0 dBTP
board = Pedalboard([
    Gain(gain_db=+6.4),
    Limiter(threshold_db=-2.0, release_ms=100),
])
```

## Stage 4: Targets

### Mix targets (pre-master):
| Metric | Target | F10 (best) |
|--------|--------|------------|
| sub/low-mid gap | 0 to +5pp | -0.4 |
| air% | >0.5 | 0.66 |
| hats% | >1.0 | 1.59 |
| LUFS | -20 to -18 | -20.6 |
| crest | >14 | 15.9 |
| peak | < -3.0 dB | -4.2 |

### Master targets:
| Metric | Target | F12 (final) |
|--------|--------|-------------|
| LUFS | -14 (Spotify) | -14.2 |
| LRA | 2-4 LU | 3.0 |
| crest | 10-12 | 11.4 |
| peak | -1.5 to -2.0 | -2.0 |
| air% | >1.0 | 1.32 |

### Known tradeoffs (mastering):
- Лимитер поднимает air и hats (тихие верха пробиваются)
- Лимитер поджимает low-mid → gap растёт (sub доминирует)
- Vocal presence проседает (подтоплен = coldwave нормально)
- LRA сжимается (6.5→3.0)

### Mastering variants (F12 vs F13 vs F14):
| | F12 | F13 | F14 |
|---|---|---|---|
| vocal% | 2.19 | 3.22 | 2.79 |
| air% | 1.32 | 1.03 | 1.31 |
| hats% | 2.63 | 1.81 | 2.83 |
| gap | 16.9 | 18.7 | 14.9 |
| LRA | 3.0 | 3.0 | 2.0 |

**F12 = финал.** Vocal подтоплен, воздух и хэты на максимуме, LRA 3.0.

## Stage 5: Analysis

**Venv:** `/tmp/audio_analysis_venv/bin/python` (librosa + pyloudnorm + pedalboard + matplotlib)

```bash
# Full SOTA analysis
/tmp/audio_analysis_venv/bin/python full_track_analysis.py track.wav

# Compare versions
/tmp/audio_analysis_venv/bin/python full_track_analysis.py new.wav --compare old.wav

# What-if simulation
/tmp/audio_analysis_venv/bin/python full_track_analysis.py track.wav --simulate "highshelf:+4"

# Band-energy (6-band)
python3 band_energy_analysis.py /tmp/mono.wav
```

**Recreate venv after reboot:**
```bash
bash setup_audio_venv.sh
```

## Key lessons
1. openDAW waveshaper мёртв в офлайн-рендере — используй pedalboard
2. HS@12k+8 — главный инструмент для воздуха. Удваивает air%, не трогает sub/gap/LUFS
3. Pedalboard bass saturation перераспределяет энергию sub→low-mid, закрывает gap
4. Лимитер +6.4 LU для Spotify. crest 16→11, LUFS -20→-14
5. Single-variable iteration — 3 changes at once = невозможно сказать что сработало
6. User applies ~1/3 recommended changes — давай RANGES (-4 to -6), не single values
7. Air/sub see-saw — boosting high-shelf уменьшает sub% математически
8. Кавер как anchor работает лучше оригинала для coldwave — темнее, плотнее
9. DattorroReverb — единственный openDAW effect что работает в офлайне
10. "ухо" не "ушо" — singular=ухо, plural=уши
