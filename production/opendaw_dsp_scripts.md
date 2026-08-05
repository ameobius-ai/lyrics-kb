# openDAW MCP DSP Scripts — Complete Reference

**111 DSP scripts** (92 Werkstatt audio effects + 9 Apparat instruments + 10 Spielwerk MIDI effects)

All scripts run on the Werkstatt/Apparat/Spielwerk scriptable device platform in openDAW.
Load via `mcp_opendaw_set_script_device_code`, control params via `mcp_opendaw_set_script_param`.

## Werkstatt (Audio Effects) — 92 scripts

### Dynamics (12)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_compressor.js` | Peak compressor with soft knee | threshold, ratio, attack, release, makeup, mix, knee |
| `werkstatt_lookahead.js` | Lookahead compressor (transparent) | threshold, ratio, attack, release, knee, makeup, mix |
| `werkstatt_limiter.js` | Brickwall limiter | ceiling, release, lookahead, dither, mix |
| `werkstatt_maximizer.js` | Maximizer (loudness, stereo link) | ceiling, release, lookahead, dither, stereo_link, mix |
| `werkstatt_exciter.js` | Harmonic exciter (saturation + HPF) | freq, harmonics, drive, mix, output |
| `werkstatt_deesser.js` | De-esser (dynamic EQ) | freq, threshold, ratio, attack, release, mix, output |
| `werkstatt_transient.js` | Transient designer | attack, sustain, mix, output |
| `werkstatt_noisegate.js` | Noise gate | threshold, attack, hold, release, range |
| `werkstatt_multiband_comp.js` | 3-band multiband compressor (LR4) | crossover1/2, low/mid/high × thr/ratio/atk/rel/gain, mix |
| `werkstatt_expander.js` | Expander (downward) | threshold, ratio, attack, release, range, mix, knee, output |
| `werkstatt_glue_comp.js` | Glue compressor (bus, warmth) | threshold, ratio, attack, release, mix, warmth, output |
| `werkstatt_bass_enhancer.js` | Bass enhancer (sub + harmonics) | freq, sub_level, direct_level, harmonics, attack, release, mix, output |

### Saturation (8)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_darksat.js` | Tape saturation/drive | drive, bias, tone, mix, output |
| `werkstatt_overdrive.js` | Tube overdrive | drive, tone, level, bias, dry |
| `werkstatt_coldfold.js` | Wavefolding + bitcrush | drive, fold, crush, slew, mix |
| `werkstatt_bitcrusher.js` | Bitcrusher + sample-rate reduction | bits, rate, drive, offset, mix |
| `werkstatt_tube_saturator.js` | Tube saturation (harmonic) | drive, warmth, bias, tone, output, mix |
| `werkstatt_fuzz.js` | Fuzz distortion | sustain, tone, octave, gate, bias, level, dry, output |
| `werkstatt_waveshaper.js` | Waveshaper (custom curve) | drive, curve, bias, harmonics, tone, output, mix |
| `werkstatt_multiband_saturator.js` | 3-band multiband saturation | crossover1/2, low/mid/high_drive, low/mid/high_char, output, mix |

### Modulation (10)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_chorus.js` | Stereo chorus | rate, depth, center, feedback, mix |
| `werkstatt_dimension_chorus.js` | Dimension chorus (dual-rate) | rate_l, rate_r, depth, center, phase_offset, width, brightness, mix, output |
| `werkstatt_flanger.js` | Flanger (comb sweep) | rate, depth, center, feedback, mix |
| `werkstatt_phaser.js` | Phaser (allpass sweep) | rate, depth, stages, base_freq, feedback, mix, stereo |
| `werkstatt_tremolo.js` | Tremolo (amplitude LFO) | rate, depth, shape, phase |
| `werkstatt_harmonic_tremolo.js` | Harmonic tremolo (freq-split) | rate, depth, crossover, shape, phase_offset, mix, output |
| `werkstatt_vibrato.js` | Vibrato (pitch LFO) | rate, depth, shape, stereo |
| `werkstatt_rotary_speaker.js` | Rotary speaker (Leslie) | speed, depth, crossover, horn_level, rotor_level, acceleration, mix |
| `werkstatt_auto_pan.js` | Auto-pan (LFO-driven) | rate, depth, shape, phase, width, offset |
| `werkstatt_auto_wah.js` | Auto-wah (envelope follower) | attack, release, min_freq, max_freq, resonance, mix |

### Reverb (6)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_reverb.js` | Plate reverb | decay, predelay, damping, width, mix |
| `werkstatt_shimmer.js` | Shimmer reverb (pitch-shifted tail) | time, feedback, pitch, shimmer, damping, mix |
| `werkstatt_spring_reverb.js` | Spring reverb (physical model) | decay, damp, tension, boing, mix |
| `werkstatt_convolution_reverb.js` | Convolution reverb (generated IR) | room_size, decay, damping, predelay, early_late, width, mix, output |
| `werkstatt_gated_reverb.js` | Gated reverb (80s drum) | decay, predelay, damping, width, threshold, hold, release, mix, output |
| `werkstatt_dereverb.js` | De-reverb (reverb reduction) | reduction, decay_est, sensitivity, bands, preserve, mix, output |

### Delay (5)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_stereo_delay.js` | Stereo delay with ping-pong | time_l, time_r, feedback, tone, mix, pingpong |
| `werkstatt_tape_delay.js` | Tape delay (wow/flutter/saturation) | time, feedback, wow, flutter, saturation, mix |
| `werkstatt_multitap_delay.js` | 4-tap delay with per-tap control | tap1-4 × time/level/pan/fb, spread, damping, mix, output |
| `werkstatt_reverse_delay.js` | Reverse delay (reverse buffer) | time, feedback, levels, pan, fade, damping, mix, output |
| `werkstatt_grain_delay.js` | Granular delay (pitch-shift grains) | delay, grain_size, grain_rate, pitch, scatter, pan, reverse, feedback, mix, output |

### EQ (5)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_paraeq.js` | Parametric EQ (3-band + HP/LP) | band1-3 × freq/gain/q, hp_freq, lp_freq, mix |
| `werkstatt_graphic_eq.js` | 10-band graphic EQ (ISO) | band_32/64/125/250/500/1k/2k/4k/8k/16k, master |
| `werkstatt_dynamic_eq.js` | Dynamic EQ (3-band, threshold-driven) | band1-3 × freq/gain/q/threshold/range, attack, release, mix, output |
| `werkstatt_tilt_eq.js` | Tilt EQ (spectral balance) | tilt, pivot, steepness, mix, output |
| `werkstatt_matching_eq.js` | Matching EQ (auto-match target) | target, match_amt, smooth, adapt_rate, tilt, mix, output |

### Filter (12)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_multifilter.js` | Multi-mode filter (LP/HP/BP/BR) | mode, cutoff, resonance, drive, mix |
| `werkstatt_moog_ladder.js` | Moog ladder filter | cutoff, resonance, drive, warmth, mode, mix |
| `werkstatt_svf.js` | State-variable filter | cutoff, resonance, morph, output_mode, drive, mix, output |
| `werkstatt_allpass.js` | Allpass filter + cascade | freq, stages, invert, feedback, mix |
| `werkstatt_dcremover.js` | DC remover + stereo width | dc_freq, width, balance, mix |
| `werkstatt_comb_filter.js` | Comb filter (feedback, damping) | freq, feedback, damping, mix, polarity |
| `werkstatt_formant_filter.js` | Vocal tract formant (vowels) | formant_a/b/c, bandwidth_a/b/c, vowel, resonance, mix |
| `werkstatt_autowah.js` | Auto-wah (multi-mode resonant) | mode, base_freq, sweep_range, sensitivity, attack, release, resonance, direction, smooth, mix, output |
| `werkstatt_modal_resonator.js` | Modal resonator (physical) | material, fundamental, decay, brightness, inharmonicity, mix, output |
| `werkstatt_envelope_follower.js` | Envelope follower | attack, release, gain, mix |
| `werkstatt_envfollower.js` | Envelope follower (with depth/threshold) | attack, release, depth, threshold, invert, makeup |
| `werkstatt_adsr_trim.js` | ADSR trimmer (dynamics shaping) | attack, decay, sustain, release, threshold, mix |

### Pitch (9)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_pitch_shift.js` | Real-time pitch shift | semitones, cents, latency, mix |
| `werkstatt_phase_vocoder.js` | Phase vocoder (pitch/formant) | pitch, formant, lock_phase, mix, output |
| `werkstatt_harmonizer.js` | Dual-voice harmonizer | shift1/2_semi, shift1/2_cent, shift1/2_gain, detune, delay, mix |
| `werkstatt_octaver.js` | Octaver (tracking, 2 octaves) | oct1, oct2, direct, smooth, track, trigger, output |
| `werkstatt_ringmod_env.js` | Ring mod + envelope follower | freq, modDepth, modRange, attack, release, threshold, mix, output |
| `werkstatt_freq_shifter.js` | Frequency shifter (Bode) | shift, direction, feedback, mix, output |
| `werkstatt_auto_tune.js` | Auto-tune (scale-aware retune) | key, scale, retune, strength, detune, mix, output |
| `werkstatt_formant_shifter.js` | Formant shifter (independent pitch) | shift, formants, pitch_tracking, brightness, width, mix, output |
| `werkstatt_vowel_morph.js` | Vowel morph (formant interpolation) | vowel, morph, rate, reso, tilt, mix, output |

### Time (4)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_granular_stretch.js` | Granular time stretch | stretch, grain, overlap, pitch, mix |
| `werkstatt_paulstretch.js` | Paulstretch (extreme time stretch) | stretch, window, mix |
| `werkstatt_time_stretch.js` | Time stretch (phase-locked) | stretch, lock_phase, transient, mix, output |
| `werkstatt_phase_vocoder.js` | Phase vocoder (also time) | pitch, formant, lock_phase, mix, output |

### Stereo (5)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_stereowidth.js` | Stereo width enhancer | width, lowTrim, lowFreq, mix, output |
| `werkstatt_multiband_imager.js` | Multiband stereo imager (3-band LR4) | crossover1/2, low/mid/high_width, bypass_low, link, mix, output |
| `werkstatt_haas_widener.js` | Haas stereo widener | delay, width, channel, feedback, mix |
| `werkstatt_mid_side_processor.js` | M/S processor (mid/side EQ) | mid_gain, side_gain, mid_freq, side_freq, width, mix |
| `werkstatt_binaural.js` | Binaural spatializer (HRTF) | azimuth, elevation, distance, head_size, room, mix, output |

### Spectral / FX (6)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_spectral_freezer.js` | Spectral freeze | freeze, smooth, spread, decay, mix, output |
| `werkstatt_spectral_blur.js` | Spectral blur (smear) | blur_size, freq_blur, time_blur, phase_rand, mix, output |
| `werkstatt_spectral_compressor.js` | Spectral compressor (per-bin) | threshold, ratio, attack, release, smoothing, tilt, mix, output |
| `werkstatt_spectral_enhancer.js` | Spectral enhancer (air + sparkle) | crossover, air, sparkle, transients, width, mix, output |
| `werkstatt_spectral_denoise.js` | Spectral denoiser | reduction, learn_time, oversub, floor, smoothing, mix, output |
| `werkstatt_spectral_gate.js` | Spectral gate (freq-selective) | bands, threshold, reduction, attack, release, min_freq, max_freq, tilt, mix, output |

### Restoration (6)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_de_plosive.js` | De-plosive (HPF + envelope) | threshold, freq, attack, release, q, mix |
| `werkstatt_declicker.js` | Declicker (median filter) | sensitivity, click_len, median_size, interp, overlap, mix, output |
| `werkstatt_decrackle.js` | Decrackler (adaptive) | strength, sensitivity, freq_est, smooth, adaptive, mix, output |
| `werkstatt_dereverb.js` | De-reverb (reverb reduction) | reduction, decay_est, sensitivity, bands, preserve, mix, output |
| `werkstatt_spectral_denoise.js` | Spectral denoiser | reduction, learn_time, oversub, floor, smoothing, mix, output |
| `werkstatt_spectral_gate.js` | Spectral gate (noise reduction) | bands, threshold, reduction, attack, release, min_freq, max_freq, tilt, mix, output |

### Physical Modeling (2)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_karplus_strong.js` | Karplus-Strong plucked string | frequency, decay, brightness, pluck_damping, stretch, mix, output |
| `werkstatt_waveguide_string.js` | Waveguide string (digital) | frequency, decay, brightness, pick_position, inharmonicity, mix, output |

### Creative FX (6)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_vocoder.js` | Channel vocoder (bandpass bank) | bands, carrier_wave, carrier_freq, mod_response, mod_threshold, band_q, emphasis, highpass, mix, output |
| `werkstatt_reverse.js` | Real-time reverse playback | chunk_size, feedback, speed, smooth, dry_gain, wet_gain, mix, stereo_mode, trigger_mode, output |
| `werkstatt_scratch.js` | DJ vinyl scratch (turntable) | depth, rate, pullback, friction, wow, flutter, flutter_rate, crackle, mix, output |
| `werkstatt_vinyl.js` | Vinyl character (age/dust/wear) | age, dust, wear, wow, flutter, noise, mix, output |
| `werkstatt_tape_stop.js` | Tape stop effect | stop_time, trigger, restart, curve, wow, flutter, flutter_rate, mix, output |
| `werkstatt_looper.js` | Looper (overdub, varispeed) | loop_length, feedback, overdub, play_mode, speed, reverse_mode, monitor, fade_edges, mix, output |

## Apparat (Instruments) — 9 scripts
| Script | Function | Key params |
|--------|----------|------------|
| `apparat_darkbass.js` | Subtractive bass synth | waveform, cutoff, resonance, attack, decay, sustain, release, subOsc, detune, volume |
| `apparat_coldlead.js` | FM lead synth | waveform, cutoff, resonance, attack, decay, sustain, release, detune, volume |
| `apparat_subcrusher.js` | Sub bass + distortion | wave, cutoff, resonance, attack, decay, sustain, release, drive, sub, glide |
| `apparat_pluck.js` | Karplus-Strong plucked string | decay, damping, brightness, attack, release, detune, volume |
| `apparat_wavetable.js` | Wavetable synth | pos, pos_lfo_rate, pos_lfo_depth, detune, unison, attack, decay, sustain, release, volume |
| `apparat_fm.js` | FM synth (carrier + modulator) | carrier, ratio, mod_depth, waveform, attack, decay, sustain, release, volume |
| `apparat_ringmod.js` | Ring modulation synth | frequency, waveform, attack, decay, sustain, release, adsrAmount, subOsc, volume |
| `apparat_supersaw.js` | Supersaw synth (detuned unison) | detune, spread, cutoff, resonance, attack, decay, sustain, release, volume |
| `apparat_bowed_string.js` | Bowed string (physical model) | bow_pressure, bow_speed, bow_position, freq, brightness, body_resonance, vibrato_rate, vibrato_depth, volume |

## Spielwerk (MIDI Effects) — 10 scripts
| Script | Function | Key params |
|--------|----------|------------|
| `spielwerk_arpeggiator.js` | Arpeggiator | rate, octaves, direction, hold, velocity, swing |
| `spielwerk_powerchord.js` | Power chord generator | interval, interval2, velScale, detune |
| `spielwerk_chorder.js` | Chord generator | chord, voicing, inversion, octave, spread, strum, velScale |
| `spielwerk_chordmemory.js` | Chord memory (hold chord) | chord, octave, velocity |
| `spielwerk_scale_quantizer.js` | Scale quantizer | scale, root, direction |
| `spielwerk_strum.js` | Strum pattern generator | speed, direction, spread, velocity |
| `spielwerk_harmonizer.js` | MIDI harmonizer (3 intervals) | interval1/2/3, vel1/2/3, mode, key_root, scale |
| `spielwerk_mididelay.js` | MIDI delay (note echoes) | time, feedback, repeats, transpose, decay |
| `spielwerk_prob_gate.js` | Probabilistic gate (stochastic) | chance, variation, seed, mode, min_pitch, max_pitch, velocity_boost, hold |
| `spielwerk_velocity.js` | Velocity scaler (scale, offset) | scale, offset, curve, min_vel, max_vel |

## DSP Chains (presets)

### Mastering chain
EQ (parametric) → Compressor → Exciter → Stereo width → Limiter

### Vocal chain
EQ (parametric) → Compressor → De-esser → Exciter → Limiter

### Lo-fi chain
Bitcrusher → Tape saturation → Tape delay (wow/flutter) → Spring reverb

### Vinyl character chain
Scratch → Reverse (triggered) → Tube saturator → Graphic EQ

### Vocoder chain
Formant filter → Vocoder (carrier: saw) → Graphic EQ → Exciter

### Drum bus chain
Transient designer → Glue compressor → Multiband saturator → Maximizer

## Usage

```python
from server import (
    mcp_opendaw_set_script_device_code,
    mcp_opendaw_set_script_param,
    mcp_opendaw_list_script_params,
)

# Load a DSP script onto a Werkstatt effect slot
with open("scripts/werkstatt_vocoder.js") as f:
    code = f.read()
await mcp_opendaw_set_script_device_code("werkstatt", 0, 0, code)

# Set parameters
await mcp_opendaw_set_script_param("werkstatt", 0, 0, "bands", 24)
await mcp_opendaw_set_script_param("werkstatt", 0, 0, "carrier_wave", 1)

# List all params
params = await mcp_opendaw_list_script_params("werkstatt", 0, 0)
```

## Categories Summary

| Category | Count | Scripts |
|----------|-------|---------|
| Dynamics | 12 | compressor, lookahead, limiter, maximizer, exciter, deesser, transient, noisegate, multiband_comp, expander, glue_comp, bass_enhancer |
| Saturation | 8 | darksat, overdrive, coldfold, bitcrusher, tube_saturator, fuzz, waveshaper, multiband_saturator |
| Modulation | 10 | chorus, dimension_chorus, flanger, phaser, tremolo, harmonic_tremolo, vibrato, rotary_speaker, auto_pan, auto_wah |
| Reverb | 6 | reverb, shimmer, spring_reverb, convolution_reverb, gated_reverb, dereverb |
| Delay | 5 | stereo_delay, tape_delay, multitap_delay, reverse_delay, grain_delay |
| EQ | 5 | paraeq, graphic_eq, dynamic_eq, tilt_eq, matching_eq |
| Filter | 12 | multifilter, moog_ladder, svf, allpass, dcremover, comb_filter, formant_filter, autowah, modal_resonator, envelope_follower, envfollower, adsr_trim |
| Pitch | 9 | pitch_shift, phase_vocoder, harmonizer, octaver, ringmod_env, freq_shifter, auto_tune, formant_shifter, vowel_morph |
| Time | 4 | granular_stretch, paulstretch, time_stretch, phase_vocoder |
| Stereo | 5 | stereowidth, multiband_imager, haas_widener, mid_side_processor, binaural |
| Spectral/FX | 6 | spectral_freezer, spectral_blur, spectral_compressor, spectral_enhancer, spectral_denoise, spectral_gate |
| Restoration | 6 | de_plosive, declicker, decrackle, dereverb, spectral_denoise, spectral_gate |
| Physical Modeling | 2 | karplus_strong, waveguide_string |
| Creative FX | 6 | vocoder, reverse, scratch, vinyl, tape_stop, looper |
| Apparat | 9 | darkbass, coldlead, subcrusher, pluck, wavetable, fm, ringmod, supersaw, bowed_string |
| Spielwerk | 10 | arpeggiator, powerchord, chorder, chordmemory, scale_quantizer, strum, harmonizer, mididelay, prob_gate, velocity |
| **Total** | **111** | |

*Updated: 2026-07-06, opendaw-mcp v1.247.0*
