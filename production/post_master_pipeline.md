# Post-Master Pipeline (scipy/numpy)

## Контекст

Suno и openDAW render дают premix с LUFS ~-12, crest ~16, DC offset. Для коммерческого мастера нужен post-render DSP: компрессия, сатурация, стерео-расширение, лимитер. Pipeline работает на готовых WAV — не требует openDAW.

## Расположение

`/home/ameobius/projects/creative-studio/agent-daw/opendaw-mcp/`
- `post_master.py` — v6 baseline (-14 LUFS)
- `post_master_pro.py` — v7 tube+M/S (-14 LUFS)
- `post_master_pro2.py` — v8 dynamic EQ+transient (-14 LUFS)
- `post_master_pro3.py` — **EXPENSIVE** (-10 LUFS, коммерческий мастер)
- `produce_stems.py` — upstream premix

## Версии

| Version | Target LUFS | Crest | Назначение |
|---------|-------------|-------|------------|
| v6 | -14 | ~16 | streaming (Spotify/YouTube) |
| pro2 | -14 | ~16.3 | streaming с характером (dyn EQ, transient, even exciter) |
| **pro3** | **-10** | **~10.8** | коммерческий мастер «дорого» |

## Цепочка pro3 (EXPENSIVE)

9 шагов:

1. **DC blocker** — HPF 20Hz 1st order, удаляет Suno DC (~0.002)
2. **LUFS pre-normalize** → target (-10 по умолчанию)
3. **Multiband split** Linkwitz-Riley 4th order (200/500/2000/5000/8000 → 6 bands)
4. **Per-band processing:**
   - sub (<200): psychoacoustic bass + transient enhancer + par.comp 4:1 + mono
   - bass (200-500): mud cut -2@250 + tube sat
   - lowmid (500-2k): +3@700 + dyn EQ -2@300 + pre-emph tape sat
   - presence (2-5k): +5@3k +4@4k +3@5k + tube + par.comp 4:1 (50/50)
   - uppermid (5-8k): +2@6k vocal clarity
   - air (>8k): highshelf +4 + even exciter +3@12k + widen 0.6
5. **Recombine + SSL-style glue comp** (ratio 2.0, mix 0.5)
6. **M/S EQ** — side HPF 200 + side boost +4@10k + widen 0.4
7. **Re-normalize** to target LUFS
8. **Soft clipper** — tanh, ceiling 0.95, drive 1.3, mix 0.7
9. **Soft-knee + oversampled limiter** — ceiling 0.891 (-1 dBFS), true peak < -1 dBTP

## Verified metrics (last_light_of_summer, 2026-07-07)

```
                LUFS    Peak    Crest   Width   Bass   Presence  Air
mix (raw)      -12.7  +1.29    16.75   0.181  -20.2   -20.1    -37.6
pro2 (-14)     -14.0  -1.19    16.31   0.273  -24.2   -21.5    -36.5
pro3 (-10)     -10.0  -2.71    10.80   0.299  -20.4   -17.5    -32.3
```

Качество (32-bit float / 48kHz / stereo сохранено, DC убран):
- DR premix 66 dB → pro3 62.7 dB (плата за громкость)
- Noise floor идентичен (-65...-70 dBFS)
- Flat-top < 0.04% — лимитер не «заморозил» сигнал

## Кастомизация

Две строки в начале `main()`:

```python
TARGET_LUFS = -10.0   # -14 streaming, -10 commercial, -8 max loud
CEILING = 0.891       # -1.0 dBFS ceiling
```

## Запуск

```bash
cd /home/ameobius/projects/creative-studio/agent-daw/opendaw-mcp
venv/bin/python post_master_pro3.py [input.wav] [output_name]
```

По умолчанию: `exports/last_light_of_summer.wav` → `exports/<base>_pro3.wav` + копия на Desktop.

## Зависимости

- `scipy`, `numpy`, `pyloudnorm` (все в `opendaw-mcp/venv/`)
- Playwright/google-chrome **не нужен** — post-master работает с файлами
- Vite сервер **не нужен** — только premix render требует openDAW

## Pitfalls

1. **premix должен существовать** — pro3 не работает из воздуха
2. **DC offset в Suno стемах** — выявлен 0.001-0.002 во всех стемах last_light. DC blocker обязателен в Step 0 (есть только в pro3, отсутствует в pro2/pro — добавлен 2026-07-07)
3. **True peak -2.42 при ceiling -1.0** — финальная LUFS-коррекция опускает gain. Нормально, означает что loudness достигнут компрессией, не пиковым лимитированием
4. **pro3 peak -2.7** — есть 1.7 dB запаса. Правь CEILING и drive если нужен пик ближе к потолку
5. **Качество сохраняется** — 32-bit float / 48kHz идёт сквозь весь pipeline, никакой конверсии
