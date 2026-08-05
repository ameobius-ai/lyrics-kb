---
id: CW-012
track: ТРИ ЦИФРЫ
playbook: synthwave / industrial
package: suno/packages/darksynth_coldwave.md
score_lyrics: null
verdict: GOOD
bpm: 118
vocal_anchor: null
stem_philosophy: null
platform: Spotify -14
status: closed
result: mastered, __Three_Digits.wav — f2 release
fail_mode: thin_low
lesson: "Dark synth-pop 118 BPM. Original master: dark spectrum, sub+bass heavy, presence hole 2-5k, air dead. Low-mids 200-500 muddy. Fix: bell cut -2@250 + high shelf +2.5@3k + high shelf +2.5@10k → presence +1.4dB, air +2.9dB, mud cleared. Limiter caught peak overshoot from shelf boost. User applied full chain in one pass, not iteratively — worked."
gen_pipeline: treblo → suno_cover_inspo
---

# CW-012 · ТРИ ЦИФРЫ

Desk-цикл M2 · статус closed.

[источник: Suno Studio, 2026-07-13]

---

## Metrics (final — __Three_Digits.wav)

| Metric | Value |
|---|---|
| LUFS | -12.6 |
| True peak | -0.6 dBTP |
| LRA | 8.1 |
| Crest | ~13 |
| BPM | 118 |
| Key | — |

## Spectral balance (final)

| Band | RMS dB |
|---|---|
| 20-80 | -20.8 |
| 80-200 | -20.2 |
| 200-500 | -23.1 |
| 500-2k | -22.5 |
| 2k-6k | -27.1 |
| 6k-12k | -28.6 |
| 12k-20k | -33.4 |

## EQ chain (actual, user-confirmed)

```
bell: -2 dB @ 250 Hz, Q 1.0      — mud / low-mid clear
high shelf: +2.5 dB @ 3k, Q 0.7  — presence / vocal
high shelf: +2.5 dB @ 10k, Q 0.7 — air / sheen
limiter: ceiling -0.5 dBTP
```

## Iteration log

1. **Original** (Три цифры.wav): -12.4 LUFS, TP -0.14, sub+bass dominant, 2k-6k -28.6, 12k-20k -38.2
2. **Edit 1** (Три цифры(1).wav): bell + shelves applied → TP +0.15 (clipping from shelf boost)
3. **Final** (__Three_Digits.wav): limiter added → TP -0.6, all bands improved

## Lesson

High shelf boost on dark source pushes peak above ceiling. Always re-check TP after any EQ boost, add limiter.
