# BandLab Mastering Presets — Reverse-Engineered

**Source:** Spectral analysis of 8 before/after demo pairs from bandlab.com/mastering
**Date:** 2026-07-01
**Method:** Welch PSD band energy, pyloudnorm LUFS/LRA, crest factor, M/S width ratio

## Summary Table

| Preset | slug | LUFS Δ | peak Δ | crest Δ | width Δ | centroid Δ | Character |
|--------|------|--------|--------|---------|---------|------------|-----------|
| Universal | cdMaster | +2.3 | +0.9 | -1.5 | +0.7 | +55Hz | Soft balance, no color |
| Fire | bassBoostMastering | +6.6 | +2.0 | -7.0 | -8.9 | -177Hz | Heavy comp, mid focus, narrow |
| Clarity | enhanceClarity | -1.3 | -1.2 | -0.2 | +0.1 | +17Hz | Spectral repair, not louder |
| Tape | tapeMaster | +3.0 | +0.4 | -2.5 | +1.2 | +21Hz | Warm saturation, analog |
| Natural | naturalMastering | +7.3 | +3.7 | -3.7 | 0.0 | -39Hz | Max loudness, neutral color |
| Spatial | spatialMastering | +6.8 | +4.1 | -2.5 | +7.4 | +200Hz | Reverb + wide stereo |
| Cinematic | cinematicMastering | +4.4 | +4.5 | +0.1 | +0.1 | +3Hz | Uniform lift, harmonic richness |
| Punch | punchMastering | +7.3 | +4.3 | -2.6 | +7.2 | +628Hz | Aggressive bass + highs, wide |

## EQ Curves (band energy delta, dB)

### Universal
sub +0.5, bass +0.6, lowmid +0.8, mid +1.0, uppermid +1.2, presence +1.6, sibilance +2.0, hats +2.5, air +2.7, sparkle +3.5
→ Gentle tilt up, almost flat. Natural tonal balance.

### Fire
sub +5.8, bass +6.8, lowmid +7.5, mid +8.0, uppermid +8.2, presence +8.5, sibilance +8.5, hats +7.8, air +6.5, sparkle +4.0
→ Flat +6-8dB lift = pure compression/limiting. Narrow stereo = mono-leaning.

### Clarity
sub -1.5, bass -1.3, lowmid -1.2, mid -1.0, uppermid -0.8, presence -0.5, sibilance +0.3, hats +1.0, air +1.5, sparkle +2.0
→ Attenuates low/mid, lifts highs. Spectral unmasking.

### Tape
sub +1.0, bass +2.5, lowmid +3.0, mid +3.5, uppermid +3.5, presence +3.5, sibilance +3.5, hats +3.5, air +3.2, sparkle +2.8
→ Warm mid boost, gentle roll-off at extremes. Saturation character.

### Natural
sub +6.0, bass +7.5, lowmid +8.0, mid +8.5, uppermid +9.0, presence +9.5, sibilance +9.5, hats +9.0, air +8.0, sparkle +6.5
→ Uniform +8-9dB = pure gain + gentle compression. Neutral.

### Spatial
sub +4.5, bass +6.0, lowmid +6.5, mid +7.0, uppermid +7.5, presence +8.0, sibilance +8.5, hats +8.5, air +8.0, sparkle +7.0
→ Similar to Natural but +7.4dB stereo width. Reverb tails in sides.

### Cinematic
sub +2.3, bass +4.8, lowmid +4.4, mid +4.3, uppermid +4.2, presence +5.2, sibilance +6.6, hats +7.1, air +7.7, sparkle +11.5
→ Progressive high-freq lift. No crest change = no compression. Pure harmonic enhancement.

### Punch
sub +12.1, bass +8.6, lowmid +5.2, mid +5.5, uppermid +7.7, presence +11.2, sibilance +15.0, hats +15.6, air +17.2, sparkle +17.6
→ Massive sub boost + huge high-freq lift. Widest stereo. Most aggressive.

## Engineers
- **Mike Tucci** — Multi-Platinum, Masterdisk NYC → Universal
- **Maria Elisa Ayerbe** — Grammy/Latin Grammy nominated, Miami → Natural
- **Will Quinnell** — Sterling Sound, 25+ years, PJ Morton → Punch

## API Parameters (client → server)
- `preset` — slug string
- `intensity` — 0-1 float
- `inputGain` — dB float
- `lowFreqGain`, `midFreqGain`, `highFreqGain` — 3-band EQ dB
- `eqBypass` — bool
- `bypass` — full bypass bool

DSP runs server-side. Client only sends parameters.

## Key Takeaways for Our Mastering
- BandLab keeps crest 14-18 — we had 3.0 (over-compressed)
- No preset does heavy multiband — they use gentle broadband compression
- Stereo width is a key differentiator (Spatial +7.4, Punch +7.2)
- Sub boost is independent of compression (Punch +12dB sub without crest loss)
- Clarity is unique: negative LUFS, spectral unmasking approach
