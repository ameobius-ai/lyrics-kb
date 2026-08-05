# Vocal Anchors — 24 готовых вокальных блока для Suno

Источник: SiliconSense (siliconsense_dump). 24 якоря: 8 MALE + 8 FEMALE + 8 SPECIAL.
Каждый — имя, сценарий, готовый `[Vocal: ...]` тег для вставки в Style box.
Заменяют одиночные слова вроде "baritone vocals" — детальный многокомпонентный блок.

## MALE

### Deep husky bass
Сценарий: rap-edge, noir pop
```
[Vocal: male, deep husky timbre, relaxed but intense delivery, clear diction, precise rhythm, modern rap-adjacent tone]
```

### Warm crooner
Сценарий: soul ballads, swing, smooth R&B
```
[Vocal: male, warm crooner baritone, jazz phrasing, slight vibrato on long notes, intimate microphone presence]
```

### Raspy rock howl
Сценарий: grunge, classic rock, alt-rock chorus
```
[Vocal: male, raspy gritty timbre, dynamic shifts from quiet verse to throat-shredding belt on chorus, anguished delivery]
```

### Airy falsetto
Сценарий: R&B, dream-pop, indie folk
```
[Vocal: male, airy floating falsetto, breathy intimate close-mic delivery, subtle stacked harmonies, vulnerable tone]
```

### Outlaw country gravel
Сценарий: country, americana, story ballads
```
[Vocal: male, gravelly weathered timbre, twangy drawl, conversational storytelling cadence, authentic and lived-in]
```

### Monotone melodic rap
Сценарий: cloud rap, alternative hip-hop, late-night vibe
```
[Vocal: male, half-sung half-rapped, monotone delivery with occasional melodic lifts, Auto-Tune subtle, introspective tone]
```

### Aggressive rap belt
Сценарий: UK drill, trap, motivational
```
[Vocal: male, aggressive articulate delivery, rapid-fire dense flows, hard vocal compression, prominent breath control, menacing edge]
```

### Anthemic theatrical
Сценарий: mid-tempo rock, cinematic pop
```
[Vocal: male, powerful tenor, dramatic dynamics, soaring belt on chorus, theatrical phrasing, slight reverb tail]
```

## FEMALE

### Soul belt
Сценарий: gospel, classic soul, R&B
```
[Vocal: female, smooth and soulful, airy on quiet lines, powerful natural belting on peaks, gospel-trained runs and ad-libs, contemporary R&B inflection]
```

### Close-mic whisper
Сценарий: bedroom-pop, ASMR, dark-pop
```
[Vocal: female, breathy whispered close-mic delivery, sibilant consonants prominent, intimate ASMR-quality, no compression]
```

### Pop power soprano
Сценарий: stadium pop, anthems, K-pop
```
[Vocal: female, bright assertive pop soprano, double-tracked anthemic choruses, polished playful phrasing, professional studio sheen]
```

### Husky alto
Сценарий: indie-folk, americana, jazz-pop
```
[Vocal: female, husky low-register alto, smoky lounge timbre, conversational phrasing, slight vibrato]
```

### Ethereal dreamy
Сценарий: dream-pop, shoegaze, ambient
```
[Vocal: female, ethereal floating delivery, heavy plate reverb, layered choir-like harmonies, no consonant attack, hazy and distant]
```

### Playful bubblegum
Сценарий: Y2K-pop, hyperpop, teen-pop
```
[Vocal: female, bright girlish timbre, coy hiccup phrasing, playful spoken ad-libs between lines, helium-light energy]
```

### Melancholic art-pop
Сценарий: tort-pop, авторские баллады
```
[Vocal: female, intimate breathy delivery, precise enunciation, minor-key melodic phrasing, no Auto-Tune, dry and present]
```

### Latin passion
Сценарий: reggaeton, salsa-pop, latin-pop
```
[Vocal: female, passionate Spanish-language delivery, expressive runs, rhythmic syncopation locked to the dembow, sultry mid-range]
```

## SPECIAL

### Robot vocoder
Сценарий: french house, electroclash, retrofuturism
```
[Vocal: heavily vocoded robotic delivery, talkbox effect, harmonized through Roland VP-330, futuristic disconnected tone]
```

### Spoken word
Сценарий: trip-hop, ambient, art-rock
```
[Vocal: spoken word delivery, no melody, contemplative pacing, close-mic dry recording, occasional whispered emphasis]
```

### Church choir
Сценарий: hymns, gospel, epic trailers
```
[Vocal: full mixed church choir, soprano-alto-tenor-bass stacked harmonies, plate reverb, sacred resonance, Latin-style enunciation]
```

### Opera soprano
Сценарий: symphonic metal, epic-pop
```
[Vocal: female, classically trained operatic soprano, controlled vibrato, full chest voice on peaks, theatrical projection]
```

### Metal scream
Сценарий: metalcore, deathcore, post-hardcore
```
[Vocal: male, alternating clean melodic vocals on chorus and aggressive growl/scream on verses, heavy distortion, throat-rending intensity]
```

### Auto-Tune wave
Сценарий: trap-soul, melodic rap
```
[Vocal: male, heavy Auto-Tune on hard fast retune setting, melodic half-sung delivery, pitch correction artifacts intentional, T-Pain-era effect]
```

### Child-like vocal
Сценарий: hyperpop, dariacore, lullaby
```
[Vocal: high-pitched child-like timbre, sing-song nursery cadence, innocent unprocessed delivery, slight pitch instability]
```

### Megaphone narrator
Сценарий: punk, industrial, agit-prop
```
[Vocal: male, megaphone-distorted shout, telephone-band-passed, urgent newsreel cadence, mid-range only]
```

---

## Как использовать

Вставить `[Vocal: ...]` блок в Style box. Можно комбинировать с delivery tags в Lyrics:
- `[Whispered]` / `[Belted]` / `[Soft]` — переключают подачу по секциям
- Persona фиксирует тембр, delivery tags управляют как он поёт в каждой секции

## Связь с базой

- `suno/vocals.md` — триггеры визга, дескрипторы, трюк с BPM
- `suno/v5-advanced.md` — v5.5 фреймворк, vocal anchor как часть архетипа
- `suno/persona.md` — фиксация голоса между генерациями
