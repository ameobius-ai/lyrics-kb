# Genre Gap Report — bitwize vs our KB/openDAW

**Date:** 2026-07-19  
**Sources:** bitwize-music-studio/claude-ai-music-skills `genres/` (~387 dirs), kb packages, openDAW arrangements (37)

## Counts

| Layer | Count |
|---|---|
| bitwize genre dirs | ~387 |
| kb packages (before) | 3 |
| kb packages (after this ship) | **9** |
| openDAW arrangements | 37 |
| openDAW GENRE_PRESETS | 9 |

## Already covered (practical)

openDAW arrangements include: house, techno, dnb, liquid_dnb, neurofunk, trap, phonk, lofi, ambient, industrial, synthwave, future_bass, breakbeat, garage, trance, kpop, jpop, metal, rock, jazz, …

kb packages had: darksynth_coldwave, folk_horror, cloud_bedroom

## Priority missing → shipped this cycle

| Package | Why |
|---|---|
| `darkwave.md` | core of RU/EU cold electronic; She Past Away lane |
| `witch_house.md` | occult lo-fi gap; Salem/ic3peak adjacent |
| `dark_ambient.md` | texture/drone layer for scores |
| `post_punk.md` | bridge rock/electronic |
| `hyperpop.md` | high-demand modern pop chaos |
| `drill.md` | street/rap practical (not phonk) |

## Still missing (next batches)

**Electronic/dark:** idm, glitch, jungle, 2-step-garage, uk-garage, hardwave, dungeon-synth, chillwave  
**Guitar/alt:** shoegaze, dream-pop, art-pop, blackgaze  
**Hip-hop:** boom-bap, abstract-hip-hop, cloud-rap, emo-rap  
**World/club:** amapiano, baile-funk, afrobeats (afrobeat arrangement exists in openDAW)  
**Metal extremes:** doom-metal, black-metal, metalcore, nu-metal  
**Other:** anisong, dark-cabaret, neofolk (partial via folk_horror)

## Policy

- Do **not** mirror all 387 bitwize dirs.
- Ship only packages with Style + Negatives + mix start + fail→fix.
- Prefer community demand (Producers Discord) over encyclopedia completeness.
- openDAW arrangements ≠ Suno packages; both can coexist.

## Source

- bitwize genre READMEs (darksynth, darkwave, witch-house) distilled into packages
- Local: `suno/packages/*.md`
