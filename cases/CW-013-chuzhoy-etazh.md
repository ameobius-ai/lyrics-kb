---
id: CW-013
track: ЧУЖОЙ ЭТАЖ
playbook: synthwave / industrial rock
package: suno/packages/darksynth_coldwave.md
score_lyrics: null
verdict: GOOD
bpm: 103
vocal_anchor: null
stem_philosophy: null
platform: Spotify -14
status: closed
result: mastered, multiple renders — best spectrum on last ru (pre-limiter)
fail_mode: thin_low
lesson: "Synthwave/industrial 103 BPM G minor. Sub overload 39% + bass 27% = 66%, gap +42pp. Presence 4.4%, air 0.5% — dead. Fix: low shelf -2.5@100 + high shelf +4@3k + high shelf +4@10k + limiter -0.5. Best render: sub 28.7%, presence 5.8%, air 1.2%, gap +24. Limiter-only variant (__Someone_elses_floor) had worse balance — sub bounced back to 38%. Full EQ stack beat limiter-only."
gen_pipeline: treblo → suno_cover_inspo
---

# CW-013 · ЧУЖОЙ ЭТАЖ

Desk-цикл M2 · статус closed.

[источник: Suno Studio, 2026-07-15]

---

## Metrics (best spectral — last ru render)

| Metric | Value |
|---|---|
| LUFS | -15.5 |
| True peak | +0.2 (pre-limiter) |
| LRA | 10.7 |
| Crest | 15.0 |
| BPM | 103.4 |
| Key | G |

## Spectral balance (best render)

| Band | Body % |
|---|---|
| sub | 28.7% |
| bass | 26.2% |
| low-mid | 10.1% |
| mid | 16.0% |
| upper-mid | 5.0% |
| presence | 5.8% |
| sibilance | 3.2% |
| hats | 3.6% |
| air | 1.2% |

## EQ chain (actual, user-confirmed)

```
low shelf: -2.5 dB @ 100 Hz, Q 0.7   — sub overload
high shelf: +4 dB @ 3 kHz, Q 0.7     — presence / vocal
high shelf: +4 dB @ 10 kHz, Q 0.7    — air / hats
limiter: ceiling -0.5 dBTP
```

## Iteration log

1. **Original** (Чужой этаж.wav): sub 39%, presence 4.4%, air 0.5%, gap +42, TP +0.2
2. **(1)** full stack applied: sub 29.6%, presence 5.2%, air 0.8%, gap +25, TP -0.1 ✅
3. **(2)** reduced to single shelf @4k: presence dropped to 4.5%, air 0.4% — worse
4. **Last ru** (+4/+4 shelves): sub 28.7%, presence 5.8%, air 1.2%, gap +24, TP +0.2 ⚠️
5. **__Someone_elses_floor** (limiter-heavy master): TP -1.8 ✅ but sub bounced to 38%

**Best for release:** last ru + limiter (or __Someone_elses_floor for streaming-ready peak).

## Lesson

1. Two shelves @+4 each > single shelf @+3 or @+4. Split frequencies (3k + 10k) cover both presence and air.
2. Aggressive limiter on already-balanced mix can反弹 sub% — limiter treats low frequencies differently.
3. User overcorrects ~1/3 of recommended gain. Recommend slightly more than needed.
