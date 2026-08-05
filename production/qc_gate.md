# Audio QC Gate (7-point)

> Source: bitwize-music-studio/claude-ai-music-skills audio quality gates
> Adapted for our post-master pipeline + openDAW exports

## Когда использовать

После render / post-master, перед релизом или экспортом на платформу.
Каждый пункт = pass/fail с конкретными порогами.

## 7 пунктов

### 1. Loudness (LUFS)
- **Measure**: pyloudnorm / measure_lufs / read_meter
- **Targets**: Spotify -14, Apple -16, YouTube -14, Club -9
- **Pass**: integrated LUFS within ±0.5 of target
- **Fail**: >1 LUFS off target

### 2. Clipping / True Peak
- **Measure**: max sample value, true peak dBTP
- **Pass**: no samples at ±1.0, true peak ≤ -0.5 dBTP (our ceiling)
- **Fail**: any digital clipping (sample = ±1.0) OR true peak > -0.3 dBTP

### 3. Silence
- **Measure**: leading/trailing silence, gaps >3s mid-track
- **Pass**: <0.5s leading, <2s trailing, no mid-track gaps
- **Fail**: >2s leading silence OR mid-track dropouts

### 4. Phase / Mono Compatibility
- **Measure**: correlation meter (stereo correlation -1..+1)
- **Pass**: average correlation > 0.3, no extended periods < 0
- **Warn**: correlation 0..0.3 (wide stereo, monitor)
- **Fail**: correlation < 0 (phase issues, mono breaks)

### 5. Stereo Width
- **Measure**: L/R balance, M/S analysis
- **Pass**: bass frequencies centered (side < 10% below 200Hz), air can be wide
- **Fail**: sub-bass in side channel (>15% side energy below 100Hz)

### 6. Frequency Balance
- **Measure**: spectrum analyzer band energy %
- **Targets** (our signature): sub+bass ~55-68%, presence 2-5%, air 2-4%
- **Pass**: bands within range
- **Warn**: one band off by 30%+
- **Fail**: sub+bass >75% (mud) or <45% (thin), air <1% (dead top)

### 7. Dynamic Range
- **Measure**: crest factor (peak/RMS ratio), LRA
- **Pass**: crest > 8 dB (dynamic), LRA > 7
- **Warn**: crest 6-8 dB (compressed but OK)
- **Fail**: crest < 6 dB (over-compressed, lifeless)

## Формат

```
 validate_export(filename) → {
   pass: bool,
   checks: [{ name, status, measured, target, detail }],
   platform_ready: { spotify: true, apple: false, ... }
 }
```

## Связь с pipeline

- После `post_master.py` / `post_master_pro2.py`
- Перед `record_lineage(kind=export)`
- Если fail → логировать метрики в lineage, НЕ блокировать (агент решает)

## Инструменты

| Check | Tool |
|-------|------|
| LUFS | `measure_lufs` (opendaw-mcp) / pyloudnorm (python) |
| Clipping | `measure_lufs` returns true_peak_db |
| Silence | python: `numpy.any(numpy.abs(samples) > 0.001)` per window |
| Phase | `werkstatt_correlation_meter.js` (opendaw-mcp) |
| Stereo | `analyze_stereo` (opendaw-mcp) |
| Freq | `analyze_spectrum` / `spectrum_analyzer.js` |
| Dynamics | `analyze_dynamics` (opendaw-mcp) |
