---
id: CW-014
track: СЧЁТЧИК ИДЁТ
playbook: synthwave / dark electronic
package: suno/packages/darksynth_coldwave.md
score_lyrics: null
verdict: EXCELLENT
bpm: 99
vocal_anchor: null
stem_philosophy: null
platform: Spotify -14
status: closed
result: mastered, post-full-stack, peak at ceiling
fail_mode: null
lesson: "Dark electronic 99 BPM F minor. Full stack (low shelf -2.5@100 + high shelf +4@3k + high shelf +4@10k) produced best spectral balance of all measured tracks: sub 14.1%, presence 11.0%, air 1.5%. No fail mode — EQ stack transformed thin_low source into balanced spectrum. Only remaining issue: peak at 0.0 dBFS — needs limiter -0.5 dBTP. No EQ needed post-stack."
gen_pipeline: treblo → suno_cover_inspo
---

# CW-014 · СЧЁТЧИК ИДЁТ

Desk-цикл M2 · статус closed.

[источник: Treblo, 2026-07-16]

---

## Metrics (post-full-stack)

| Metric | Value |
|---|---|
| LUFS | -14.8 |
| True peak | 0.0 (at ceiling) |
| LRA | 7.5 |
| Crest | 15.3 |
| BPM | 99.4 |
| Key | F |

## Spectral balance (post-stack)

| Band | Body % |
|---|---|
| sub | 14.1% |
| bass | 18.3% |
| low-mid | 25.2% |
| mid | 12.8% |
| upper-mid | 6.3% |
| presence | 11.0% |
| sibilance | 5.3% |
| hats | 5.4% |
| air | 1.5% |

**sub/low-mid gap: -12pp** — mids dominant, not sub. Different balance from CW-012/013. Healthiest spectrum of all measured tracks.

## EQ chain (actual, user-confirmed — full stack applied before measurement)

```
low shelf: -2.5 dB @ 100 Hz, Q 0.7
high shelf: +4 dB @ 3 kHz, Q 0.7
high shelf: +4 dB @ 10 kHz, Q 0.7
limiter: ceiling -0.5 dBTP (pending — peak at 0.0)
```

## Lesson

Full stack works as universal starting point for dark/thin AI generations, but not every track needs it. This track arrived already post-stack — confirming the recipe transforms thin_low sources reliably. Presence 11% is the highest measured — benchmark for vocal clarity.
