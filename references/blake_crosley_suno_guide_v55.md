# Blake Crosley — Suno Guide: Tags, Meta Tags & Prompts (V5.5)

> Полный справочник (14.6k слов, 73 мин чтения). Оригинал: https://blakecrosley.com/guides/suno
> Обновлено автором: 2026-07-25 (TL;DR мая 2026). Сохранено: 2026-08-04.
> Русский дистиллят: suno/blake_crosley_v55.md

---

# Suno Guide: Tags, Meta Tags & Prompts (V5.5)

# Every Suno tag and meta tag that works in V5.5: style prompts, structure tags, [no vocals], the style-of-music field, and MILO-1080 — with copy-paste examples.

author: [Blake Crosley](/about) words: 14599 read\_time: 73m updated: 2026-07-25 00:00

$ less suno-ai-music-generation.md

*Updated May 13, 2026*

> **TL;DR:** Suno generates full songs (vocals, instruments, arrangement, and mix) from text prompts. V5.5 produces studio-grade audio with up to 8 minutes per generation, and adds Voices, Custom Models, and My Taste adaptive preferences. Master three systems (prompt text + metatags + Creative Sliders) and Suno becomes a production tool, not a novelty. Use Custom Mode for control, metatags for song structure, and the Song Editor for iterative refinement. Pro tier ($10/month, or $8/month annual) enables V5.5 and commercial rights. Credits don’t roll over.

Suno’s 2 million paid subscribers generate 7 million tracks per day, surpassing Spotify’s entire 100-million-song catalog every two weeks.[18](#fn:18) V5 crossed a threshold that earlier versions couldn’t: output that listeners engage with without realizing it was AI-generated.[1](#fn:1) Not as a curiosity or placeholder, but as actual music used in production contexts.

The difference between “interesting AI music” and “music I’d actually release” comes down to understanding three control systems:

1. **Prompt text**: Genre, mood, instrumentation, and vocal style described in natural language
2. **Metatags**: Structural directives like `[Verse]`, `[Chorus]`, `[Bridge]` that control arrangement
3. **Creative Sliders**: Weirdness, Style Influence, and Audio Influence that shape the generation’s personality

The default workflow (type a sentence, click generate) produces hit-or-miss results because Suno optimizes for broad appeal, not for what you specifically want. Precision is what separates usable output from random results.

I’ve generated thousands of tracks across every genre Suno supports, tested every metatag combination documented and undocumented, and mapped the boundaries of what each model version handles well and poorly. This guide distills that experience into the definitive technical reference.

---

## Key Takeaways

* **Custom Mode is mandatory for serious work.** Simple Mode strips away the controls that make Suno a production tool. Every technique in this guide assumes Custom Mode with separate Style, Lyrics, and Title fields.
* **Three control systems, not one.** Prompt text defines the musical character. Metatags control arrangement and structure. Creative Sliders shape the generation’s personality. Mastering all three is what separates usable output from random results.
* **Metatags are the highest-impact skill.** A `[Verse]`/`[Chorus]`/`[Bridge]` structure with parameterized modifiers (`[Verse: whispered vocals, acoustic guitar only]`) gives you per-section control that approaches DAW-level arrangement through text alone.
* **V5.5 is the current flagship.** Building on V5’s production-quality foundation (studio-grade audio, natural vocals, real instrument separation), V5.5 adds Voices, Custom Models personalized to your style, and My Taste adaptive preferences. Pro tier ($10/month, or $8/month annual) is required for V5.5 access, Voices, and Custom Models.
* **Iterate, don’t pray.** The generation loop (ideate -> select -> refine -> extend -> edit -> export) typically costs 50–100 credits per polished track. Budget for iteration, not single-shot perfection.
* **Credits don’t roll over, but top-ups don’t expire.** Monthly credits reset at each billing cycle. Purchased top-up credits persist as long as your subscription is active, making top-ups useful for stockpiling before intensive sessions.[13](#fn:13)

---

## How to Use This Guide

| You are… | Start here | Then explore |
| --- | --- | --- |
| **Brand new to Suno** | [Getting Started](#getting-started), [The Prompt Architecture](#the-prompt-architecture) | [Suno Tags and Meta Tags](#suno-tags-and-meta-tags), [Genre and Style Descriptors](#genre-and-style-descriptors) |
| **Casual user wanting better results** | [The Prompt Architecture](#the-prompt-architecture), [Creative Sliders](#creative-sliders) | [Advanced Metatag Patterns](#advanced-metatag-patterns), [Troubleshooting](#troubleshooting) |
| **Producing music for release** | [The Generation Loop](#the-generation-loop), [Suno Studio DAW](#suno-studio-daw) | [DAW Integration](#daw-integration), [Commercial Licensing](#commercial-licensing) |
| **Evaluating Suno vs. alternatives** | [What is Suno?](#what-is-suno), [Competitors and Alternatives](#competitors-and-alternatives) | [API and Integration Status](#api-and-integration-status), [Copyright and Legal Landscape](#copyright-and-legal-landscape) |

---

## Table of Contents

### Part 1: Foundations

1. [What is Suno?](#what-is-suno)
2. [Getting Started](#getting-started)
3. [Models and Versions](#models-and-versions)
4. [Pricing and Credits](#pricing-and-credits)

### Part 2: Prompt Engineering

1. [The Prompt Architecture](#the-prompt-architecture)
2. [Prompt Enhancement Helper](#prompt-enhancement-helper)
3. [Genre and Style Descriptors](#genre-and-style-descriptors)
4. [Vocal Styling](#vocal-styling)
5. [Instrumental Mode](#instrumental-mode)

### Part 3: Song Structure

1. [Suno Tags and Meta Tags](#suno-tags-and-meta-tags)
2. [Structural Tags](#structural-tags)
3. [Instrumental and Vocal Tags](#instrumental-and-vocal-tags)
4. [Advanced Metatag Patterns](#advanced-metatag-patterns)

### Part 4: Creative Controls

1. [Creative Sliders](#creative-sliders)
2. [Song Editor](#song-editor)
3. [Covers and Remixes](#covers-and-remixes)
4. [Voices](#voices)
5. [My Taste (V5.5)](#my-taste-v55)

### Part 5: Production Workflows

1. [The Generation Loop](#the-generation-loop)
2. [Suno Studio DAW](#suno-studio-daw)
3. [Stem Separation and Export](#stem-separation-and-export)
4. [DAW Integration](#daw-integration)

### Part 6: Advanced Techniques

1. [Genre Blending](#genre-blending)
2. [Multi-Section Composition](#multi-section-composition)
3. [Prompt Chaining](#prompt-chaining)
4. [Troubleshooting](#troubleshooting)

### Part 7: Business and Legal

1. [Commercial Licensing](#commercial-licensing)
2. [Copyright and Legal Landscape](#copyright-and-legal-landscape)
3. [Competitors and Alternatives](#competitors-and-alternatives)

### Part 8: Reference

1. [API and Integration Status](#api-and-integration-status)
2. [Quick Reference Card](#quick-reference-card)
3. [Changelog](#changelog)
4. [References](#references)

---

## What is Suno?

Suno is a generative AI platform that creates complete songs from text descriptions. Unlike DAWs, sample libraries, or loop-based tools, Suno generates every element of a track simultaneously: melody, harmony, rhythm, instrumentation, vocals (with lyrics), arrangement, and mix. You describe what you want; Suno produces a finished song.

### How does Suno compare to traditional music production?

| Aspect | Suno | Traditional Production |
| --- | --- | --- |
| **Input** | Text prompt + optional lyrics | Notes, MIDI, audio recordings |
| **Output** | Complete mixed song | Individual tracks needing mixing |
| **Time to first output** | ~30 seconds | Hours to days |
| **Musical knowledge required** | Descriptive vocabulary | Instrument proficiency, theory, mixing |
| **Iteration method** | Re-prompt, edit sections, adjust sliders | Re-record, re-arrange, re-mix |
| **Maximum length** | 8 minutes per generation (extendable; Duration slider on web sets target length) | Unlimited |

**What you can create:**

* **Full songs with vocals**: Any genre, any language, original lyrics or AI-generated
* **Instrumentals**: Background music, scores, ambient tracks
* **Genre experiments**: Cross-genre fusions that would require multiple specialist musicians
* **Variations**: Generate dozens of takes on the same concept, pick the best
* **Production elements**: Stems for use in traditional DAW workflows

**What Suno is not:**

* **Not a DAW**: You don’t mix, master, or arrange manually (though Studio adds some of this)
* **Not deterministic**: The same prompt produces different results each time
* **Not a sample library**: You can’t isolate and reuse individual sounds precisely
* **Not unlimited**: Generation costs credits, and quality varies between attempts

---

## Getting Started

### Quick start (5 minutes)

1. **Create an account** at [suno.com](https://suno.com). Free tier gives 50 credits per day (approximately 10 songs, usually five two-song Create batches).
2. **Try Simple Mode first.** Type a short description like “upbeat indie rock song about a road trip” and click Create. Suno generates lyrics, melody, arrangement, and vocals automatically.
3. **Switch to Custom Mode** for control. Custom Mode separates the prompt into distinct fields:
4. **Style of Music**: Genre, mood, instrumentation descriptors
5. **Lyrics**: Your lyrics with metatags for structure
6. **Title**: Song title
7. **Listen to both outputs.** Suno generates two variations per creation. Pick the one closer to your intent, then refine.
8. **Set a target length (web).** Drag the Duration slider in the Create form to pick your song’s length before generating. Available on web with the V5.5 model (added July 20, 2026).[41](#fn:42) Before the slider, length was model-determined and only adjustable after generation.
9. **Use Extend** to continue a song beyond its initial generation, or **Song Editor** to replace specific sections.

### Interface overview

Suno’s web interface has two primary creation modes:

**Simple Mode**: One text box. Describe the song in natural language. Suno infers genre, writes lyrics, and generates everything. Good for exploration, bad for precision.

**Custom Mode**: Three separate fields (Style, Lyrics, Title) plus Creative Sliders. Custom Mode is where serious work happens. The Style field accepts genre and production descriptors. The Lyrics field accepts text with metatags. The sliders control generation personality.

> **Start with Custom Mode.** Simple Mode is convenient but strips away the controls that make Suno useful for production work. Every technique in this guide assumes Custom Mode.

---

## Models and Versions

Suno has iterated rapidly since launch. Each version brings meaningful quality improvements, but access varies by subscription tier.

### Version timeline

| Version | Release | Key Improvements |
| --- | --- | --- |
| **V2** | Fall 2023 | First public model. Short clips (~30s), limited genre range, obvious AI artifacts. |
| **V3** | March 2024 | Extended to 2 minutes. Improved vocal clarity. Expanded genre coverage. |
| **V3.5** | Summer 2024 | Better mixing, reduced artifacts, improved vocal naturalness. |
| **V4** | November 19, 2024 | Major quality jump. 4-minute generations, multilingual vocals, Covers feature, 2-stem separation. |
| **V4.5** | May 1, 2025 | 8-minute single generation (up from 4 min), Creative Sliders (Weirdness, Style Influence), Prompt Enhancement Helper, expanded genre accuracy, enhanced vocals.[19](#fn:19) |
| **V4.5-All** | Late 2025 | Free tier model. Combines V4.5 improvements with broader access. |
| **V5** | September 2025 | Studio-grade audio[20](#fn:20), higher mastered quality, Suno Studio DAW[2](#fn:2), 12-stem separation[22](#fn:22), Persona Voices[15](#fn:15). Internal name: chirp-crow.[20](#fn:20) |
| **V5.5** | March 26, 2026 | Current flagship. Voices with verification (Pro/Premier), Custom Models (up to 3 per Pro/Premier subscriber), My Taste adaptive preference system (all users).[30](#fn:30)[31](#fn:31) |

### Current model access

| Tier | Model Access | Quality Notes |
| --- | --- | --- |
| **Free** | V4.5-All | Good quality, noticeably below V5.5 in vocal naturalness and mix clarity. No Voice Cloning or Custom Models. My Taste available. |
| **Pro** ($10/mo) | V5.5 | Studio-grade quality. Voices, up to 3 Custom Models, My Taste. |
| **Premier** ($30/mo) | V5.5 + Studio | Same generation quality as Pro, plus Suno Studio DAW. Voices, up to 3 Custom Models, My Taste. |

> **V5 is a meaningful upgrade over V4.5.** The difference is most audible in vocal naturalness (less “AI singer” quality), low-frequency clarity (bass and kick separation), and stereo imaging. If you’re evaluating Suno for production use, evaluate on V5, not the free tier.

### What V5 changed

V5 (internally called “chirp-crow”[20](#fn:20)) represents Suno’s largest single-version improvement:[1](#fn:1)

* **Studio-grade audio fidelity**: V5 ships at a higher mastered quality than V4.5; official docs describe the improvement in production terms rather than naming a specific sample rate. A third-party Suno product hub lists 44.1 kHz for V5; if the exact rate matters for your pipeline, inspect an exported WAV.[16](#fn:16)[20](#fn:20)
* **Vocal naturalness**: Reduced the “uncanny valley” quality that marked previous versions. Vibrato, breath sounds, and consonant articulation are more convincing.[1](#fn:1)
* **Instrument separation**: Individual instruments in the mix are more distinct. Less “wall of sound” blending.[1](#fn:1)
* **Dynamic range**: Better handling of quiet-to-loud transitions. Previous versions tended to compress everything.[1](#fn:1)
* **Genre accuracy**: Better adherence to genre conventions. A “jazz” prompt sounds more authentically jazz, not “pop with jazz chords.”[19](#fn:19)
* **Suno Studio**: In-browser DAW for post-generation editing. Mix adjustment, stem isolation, and arrangement changes without re-generating.[2](#fn:2)

### What V5.5 changed

V5.5 (March 26, 2026) builds on V5’s audio quality foundation with three personalization features:[30](#fn:30)[31](#fn:31)

* **Voices**: Clone or reuse your own voice for use in generations. Suno requires verification by comparing a spoken phrase against the uploaded or live-captured vocal sample. Pro/Premier only, v5.5 model required, and availability is restricted by age and location. In the Create menu, the **Voices** button has replaced the Personas button, though Style Personas remain accessible within the Voices menu.[31](#fn:31)
* **Custom Models**: Train up to 3 personalized versions of V5.5 based on songs from your catalog or tracks made outside Suno. Suno’s current v5.5 announcement says Custom Models need at least six songs; use stylistically consistent tracks rather than mixing random genres, because the model is learning your sound, not a grab bag of unrelated references.[30](#fn:30)[31](#fn:31)
* **My Taste**: An adaptive preference system available to all users. Learns from your favorite genres, moods, and creation/listening habits to bias future generations toward your preferred styles, production aesthetics, and vocal qualities. The magic wand icon at the top right of the Styles box generates a personalized style description when Style Augmentation is enabled. My Taste is enabled by default and can be edited or disabled from the avatar menu.[31](#fn:31)

---

## Pricing and Credits

> **Verified as of May 2026.** Suno pricing changes without notice. Check [suno.com/pricing](https://suno.com/pricing) for current rates.[13](#fn:13)

### Plan comparison

| Feature | Free | Pro ($10/mo) | Premier ($30/mo) |
| --- | --- | --- | --- |
| **Annual billing** | N/A | $8/mo ($96/yr) | $24/mo ($288/yr) |
| **Credits** | 50/day | 2,500/month | 10,000/month |
| **Model** | V4.5-All | V5.5 | V5.5 |
| **Songs included** | 10/day | Up to 500/month | Up to 2,000/month |
| **Concurrent songs** | 4 in shared queue | 10 in priority queue | 10 in priority queue |
| **Audio upload limit listed on pricing page** | Up to 8 min | Up to 30 min | Up to 30 min |
| **Song Editor** | Limited | Full | Full |
| **Covers/Remixes** | No | Yes | Yes |
| **Persona Voices** | No | Yes | Yes |
| **Voice Cloning** | No | Yes | Yes |
| **Custom Models** | No | Up to 3 | Up to 3 |
| **My Taste** | Yes | Yes | Yes |
| **Suno Studio** | No | No | Yes |
| **Stem Separation** | Split from Mix (2) | Split from Mix + Auto Split (12) | Split from Mix + Auto Split + Advanced Split (~100) |
| **Commercial use** | No | Yes | Yes |
| **Priority generation** | No | Yes | Yes |
| **Credit rollover** | N/A | No | No |
| **Top-up credits** | No | Yes | Yes |

### Credit economics

Each song costs approximately **5 credits**. A typical Create action returns two song variations, so budget about **10 credits per two-song batch**. A Pro subscription’s 2,500 monthly credits yields up to **500 songs**.[13](#fn:13)

**Credit-efficient practices:** - Use Custom Mode with specific prompts to reduce throw-away generations - Extend promising tracks rather than re-generating from scratch - Use the Song Editor to fix sections rather than regenerating entire songs - Save credits by refining your Style prompt before generating

**Monthly credits do not roll over.** Unused credits at the end of a billing cycle are lost. Plan your generation sessions accordingly.

**Bonus daily credits when monthly allocation is exhausted.** Once your monthly credits run out, paid subscribers receive 50 bonus credits per day until the next billing cycle, the same daily allocation as the free tier. This prevents a complete generation blackout at the end of the month, though it’s a significant reduction from the monthly rate (50/day vs ~83/day for Pro, ~333/day for Premier).[24](#fn:24)

**Top-up credits do not expire while your subscription remains active.** Purchased credit top-ups require an active subscription to use. If you cancel your subscription, top-up credits become unusable until you resubscribe. The persistence makes top-ups useful for stockpiling before intensive production sessions.[13](#fn:13)

---

## The Prompt Architecture

Suno’s Custom Mode splits your creative input into three fields, each serving a distinct purpose. Understanding what goes where (and what doesn’t) is the difference between hit-or-miss results and consistent output.

### The Style field

The Style field defines the musical character of your generation. It accepts natural language descriptors for genre, mood, tempo, instrumentation, vocal quality, and production style.

**The optimal formula:**

```
[Genre]  [Subgenre],  [Tempo/ Energy],  [Key  instruments],  [Vocal  style],  [Production  quality],  [Mood]
```

**Example:**

**Descriptor sweet spot: 4–7 descriptors.** Fewer than 4 gives Suno too much latitude. More than 7 and descriptors start competing with each other, producing muddy results where no single quality comes through clearly.[14](#fn:14)

### Before and after: prompt precision matters

The same creative intent produces vastly different results depending on Style field precision:

**Vague prompt (2 descriptors):**

**Result:** Generic pop-rock with standard drums, distorted guitar, and a male vocal defaulting to radio-friendly tone. Suno fills every unspecified parameter with its most popular default. Across 10 generations, no two sound related.

**Precise prompt (6 descriptors):**

**Result:** Consistent garage rock with identifiable lo-fi character. Drums sound room-mic’d, bass is dominant, vocals are raw. Across 10 generations, all share a recognizable sonic identity. The differences are in melody and arrangement, not fundamental character.

**Why the difference:** Each descriptor constrains one dimension of the output. “Rock” alone leaves tempo, vocal style, production quality, instrument balance, and mood entirely up to Suno. Adding “garage” constrains subgenre conventions, “lo-fi production” constrains sonic texture, “shouted male vocals” constrains vocal delivery. The model has less room to default to generic choices.

**Over-specified prompt (10+ descriptors):**

**Result:** Muddy compromise. Suno can’t honor all constraints simultaneously, so it partially satisfies each one. The “1960s Detroit influence” may conflict with “145 BPM,” and “reverb-heavy” fights “lo-fi production.” The output sounds confused rather than specific.

### What works in the Style field

| Descriptor Type | Examples | Effect |
| --- | --- | --- |
| **Genre** | rock, jazz, hip-hop, EDM, classical, country | Primary musical framework |
| **Subgenre** | shoegaze, bossa nova, trap, dubstep, baroque | Narrows genre conventions |
| **Tempo** | slow, mid-tempo, upbeat, fast, 120 BPM | Controls speed (BPM values are approximate, not exact) |
| **Instruments** | acoustic guitar, synth pad, brass section, strings | Suggests instrumentation (not guaranteed) |
| **Vocal quality** | raspy male vocals, ethereal female vocals, choir | Shapes vocal character |
| **Production** | lo-fi, polished, raw, overdriven, clean | Overall sonic texture |
| **Mood** | melancholic, euphoric, aggressive, dreamy, dark | Emotional tone |
| **Era** | 80s, 90s grunge, 2000s pop, vintage, modern | Period-specific conventions |

### What doesn’t work in the Style field

* **Specific artist names**: “Sounds like Adele” is unreliable and may be filtered. Use descriptive equivalents: “powerful female vocal, piano-driven pop ballad”
* **Technical mixing terms**: “Sidechain compression on the kick” is ignored. Suno doesn’t interpret mixing parameters
* **Exact BPM control**: “127 BPM” is treated as approximate guidance, not a metronome lock
* **Negative instructions**: “No drums” in the Style field is unreliable. Use the official **Exclude** field under Advanced Options for unwanted instruments and elements, the Instrumental toggle for full-track structure, or metatags for section-level control

### The Lyrics field

The Lyrics field accepts your song text with optional metatags for structural control. Without metatags, Suno infers structure from line breaks and content patterns.

**Basic lyrics (no metatags):**

**Lyrics with metatags (recommended):**

```
[Verse 1] Walking down the empty road Headlights fading in the rain[Chorus]Keep driving, keep driving Through the storm and through the night[Verse 2] Every mile feels like a year But the horizon's getting bright[Chorus]Keep driving, keep driving Through the storm and through the night[Outro] And the sun comes up again
```

> **Always use metatags.** Without them, Suno makes structural decisions that may not match your intent. A `[Chorus]` tag ensures repetition and melodic emphasis. A `[Bridge]` tag signals a harmonic departure. These structural cues dramatically improve output consistency.

### The web Lyrics Editor (July 2026)

In July 2026 Suno redesigned lyric writing on the web around a dedicated Lyrics Editor.[40](#fn:41) Five additions matter for the workflow in this guide:

* **Lyricist**: a profile that saves and locks in your writing style, so successive lyric sessions keep a consistent voice instead of resetting to Suno’s default register each time.
* **Natural-language editing**: type an instruction like “make this line funnier” and the editor applies the change in place — no manual rewrite-and-paste loop.
* **Rhyme and alternate-phrasing suggestions**: highlight a word or line to get rhyme options and alternate phrasings for it.
* **Song structure labels**: tag sections as Verse, Chorus, or Outro to tell the model how the track should flow. These labels are the editor’s point-and-click surface for the same job the bracket metatags above do in a plain-text lyric sheet — see [Suno Tags and Meta Tags](#suno-tags-and-meta-tags) for how the two surfaces relate.
* **Distraction-free full-screen editor with autosave**: a full-screen writing mode that saves as you type.

The editor changes how you produce a lyric sheet, not what the model accepts: a fully tagged plain-text sheet like the examples above still pastes straight into the Lyrics field and works exactly as before.

### The Title field

The Title field names your generation. It has minimal effect on the musical output but appears in metadata and Suno’s library. Keep it descriptive for your own organization.

---

## Prompt Enhancement Helper

Introduced in V4.5, the Prompt Enhancement Helper is an AI-powered feature that rewrites your Style field prompt before generation. When enabled, Suno expands your descriptors into a more detailed prompt that the model can interpret more precisely.[14](#fn:14)

### How it works

1. You write a Style prompt: `indie rock, energetic`
2. The Helper expands it to something like: `Energetic indie rock, driving electric guitars, punchy drums, dynamic bass, bright and raw production, anthemic and youthful`
3. Suno generates from the expanded prompt, not your original

### When to use it

| Scenario | Use Helper? | Why |
| --- | --- | --- |
| Short, vague prompts | **Yes** | The Helper adds specificity you didn’t provide |
| Exploring a new genre | **Yes** | Surfaces descriptors you might not know |
| Precise, detailed prompts (5+ descriptors) | **No** | The Helper may override or dilute your intent |
| Repeating a known-good Style prompt | **No** | You want consistency, not reinterpretation |

### Important behavior

* The Helper is **non-deterministic**: it rewrites differently each time, even for the same input
* You can **view the expanded prompt** after generation to learn what descriptors Suno found useful
* The expanded prompt is a good learning tool: generate once with the Helper, read the expansion, then use those descriptors directly in future prompts without the Helper
* **Disable it for production work** where you want exact control over what Suno receives

> **Use the Helper to learn, not to rely on.** Extract useful descriptors from its expansions, add them to your own vocabulary, and write precise prompts yourself. The best results come from prompts you control entirely.

---

## Genre and Style Descriptors

Suno recognizes hundreds of genre and style terms. Research shows approximately 86% of AI music model training data comes from Global North genres, with instruments like guitar, piano, and drums comprising 52–67% of training clips while regional instruments represent less than 3%.[21](#fn:21) Genre accuracy varies by specificity and cultural origin as a direct consequence.

### High-confidence genres (consistent results)

These genres produce reliably accurate outputs because they’re well-represented in training data:

| Genre | Effective Descriptors | Notes |
| --- | --- | --- |
| **Pop** | pop, synth-pop, indie pop, dream pop, electropop | Suno’s strongest genre. Default behavior trends toward pop if unspecified. |
| **Rock** | rock, indie rock, alt-rock, classic rock, punk rock, post-punk | Good instrument separation. Guitar tones are convincing. |
| **Hip-Hop/Rap** | hip-hop, trap, boom bap, lo-fi hip-hop, conscious rap | Rap vocals work well in V5. Flow and delivery are controllable via lyrics formatting. |
| **Electronic/EDM** | EDM, house, techno, trance, drum and bass, dubstep | Strong at build-drop structures. Synth textures are varied. |
| **R&B/Soul** | R&B, neo-soul, contemporary R&B, motown | Smooth vocal quality. Good at groove-based arrangements. |
| **Country** | country, country rock, outlaw country, bluegrass | Acoustic instruments are well-rendered. Pedal steel and banjo are recognizable. |
| **Folk** | folk, indie folk, folk rock, Americana | Acoustic focus. Natural vocal styles. |
| **Jazz** | jazz, smooth jazz, jazz fusion, bebop, swing | Improved significantly in V5. Harmonic complexity is audibly better than V4. |

### Medium-confidence genres (usable with guidance)

| Genre | Effective Descriptors | Notes |
| --- | --- | --- |
| **Metal** | metal, heavy metal, death metal, black metal, metalcore | Distorted guitar tones work well. Extreme vocals (growls, screams) are hit-or-miss. |
| **Classical** | classical, orchestral, chamber music, symphony | Good at basic orchestral arrangements. Complex counterpoint is weak. |
| **Latin** | reggaeton, salsa, bossa nova, cumbia, bachata | Rhythm patterns are generally accurate. Instrument specificity varies. |
| **Afrobeats** | afrobeats, afropop, highlife | Improving. Rhythm accuracy is better in V5 than V4. |
| **K-Pop/J-Pop** | K-pop, J-pop, city pop | Production style is recognizable. Vocal language may default to English unless lyrics specify otherwise. |

### Low-confidence genres (requires iteration)

| Genre | Effective Descriptors | Notes |
| --- | --- | --- |
| **Microtonal/Avant-garde** | avant-garde, experimental, noise | Unpredictable. Results are creative but rarely match intent. |
| **Traditional/Folk (non-Western)** | gamelan, raga, Tuvan throat singing | Limited training data. Results are approximations rather than authentic recreations. |
| **Sound design/SFX** | ambient drone, soundscape | Better handled by Stable Audio. Suno optimizes for song structure. |

---

## Vocal Styling

Vocal character is one of the most controllable aspects of Suno output. V5 significantly improved vocal naturalness and expressiveness.

### Vocal descriptors

| Descriptor | Effect |
| --- | --- |
| **Gender** | “male vocals”, “female vocals”, “androgynous vocals” |
| **Tone** | “warm”, “bright”, “dark”, “rich”, “thin”, “breathy” |
| **Technique** | “raspy”, “smooth”, “vibrato”, “falsetto”, “belt”, “whisper” |
| **Style** | “soulful”, “punk”, “operatic”, “conversational”, “spoken word” |
| **Processing** | “reverb-heavy”, “dry vocals”, “auto-tuned”, “distorted”, “lo-fi” |
| **Harmony** | “harmonized”, “choir”, “backing vocals”, “vocal layering” |

### Combining vocal descriptors

Stack 2–3 vocal descriptors for precise control:

### Language and multilingual vocals

Suno V5 supports multilingual vocal generation. The model infers language from your lyrics. For non-English lyrics:

* Write lyrics in the target language in the Lyrics field
* Optionally add the language to the Style field: “Japanese city pop, female vocals”
* Expect best results in English, Spanish, Portuguese, French, Japanese, Korean, and Mandarin
* Lesser-represented languages may produce accented or imprecise pronunciation

---

## Instrumental Mode

Toggle **Instrumental** in Custom Mode to generate tracks without vocals. The Style field becomes the only creative input.

### When should you use instrumental mode?

* **Background music**: Podcast intros, video scores, ambient work music
* **Production elements**: Beat beds, chord progressions, atmospheric textures
* **Genre exploration**: Test genre descriptors without vocal quality as a variable
* **DAW integration**: Generate backing tracks for live vocal recording

### Instrumental prompt patterns

Without vocals, the Style field needs more descriptive detail to compensate:

> **Tip:** Even in instrumental mode, add `[Instrumental]` or `[Instrumental Break]` metatags in the Lyrics field to reinforce the intent and control arrangement structure.

---

## Suno Tags and Meta Tags

Suno’s tags (written “metatags” in most Suno documentation, “meta tags” in most search queries; the terms are interchangeable) are its structural control language. Placed in the Lyrics field inside square brackets, they direct arrangement, instrumentation, dynamics, and vocal behavior. Metatags convert Suno from a prompt-to-song toy into a composition tool.[10](#fn:10)

Suno has two tag systems living in two different fields:

* **Meta tags** go in the **Lyrics field** inside square brackets: `[Verse]`, `[Chorus]`, `[Guitar Solo]`, `[Fade Out]`. They control song structure and per-section behavior. This section and the three that follow are the complete reference.
* **Style tags** go in the **Style field** as plain descriptors with no brackets: genre, tempo, instrumentation, vocal quality, production, mood. They control the overall musical character. See [The Prompt Architecture](#the-prompt-architecture) and [Genre and Style Descriptors](#genre-and-style-descriptors) for the full style vocabulary.

### Suno tags at a glance

Copy-paste any of these into the Lyrics field:

| Category | Common tags | Copy-paste example |
| --- | --- | --- |
| **Structure** | `[Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Outro]`, `[End]` | `[Chorus]` on its own line before your hook lyrics |
| **Instrumental** | `[Instrumental]`, `[Instrumental Break]`, `[Guitar Solo]`, `[Piano Solo]`, `[Synth Solo]` | `[Instrumental Break]` between verse 2 and the bridge |
| **Vocal** | `[Male Vocal]`, `[Female Vocal]`, `[Choir]`, `[Harmony]`, `[Rap]`, `[Whisper]`, `[Spoken Word]` | `[Whisper]` before a quiet, intimate line |
| **Dynamics and production** | `[Fade In]`, `[Fade Out]`, `[Crescendo]`, `[Silence]`, `[Key Change]`, `[Tempo: slow]` | `[Fade Out]` as the last line of the outro |
| **Parameterized** | `[Verse: whispered vocals, acoustic guitar only]`, `[Chorus: full band, soaring vocals]` | Add `: descriptors` inside any structural tag for per-section control |

The full tables live in the next three sections: [Structural Tags](#structural-tags) for every section tag, [Instrumental and Vocal Tags](#instrumental-and-vocal-tags) for instrument and voice control, and [Advanced Metatag Patterns](#advanced-metatag-patterns) for parameterized tags and dynamics.

### Copy-paste starter: a fully tagged lyric sheet

```
[Intro: sparse, atmospheric][Verse 1] Your first verse lyrics here[Chorus] Your hook lyrics here[Verse 2] Your second verse lyrics here[Chorus]Your hook lyrics here (same text encourages melodic repetition)[Bridge: stripped down, different energy] Your contrast lyrics here[Chorus] Your hook lyrics here[Outro: fade out][End]
```

### Is there a `[no vocals]` tag?

There is no dedicated `[no vocals]` meta tag, and writing “no vocals” in the Style field is unreliable (negative instructions there tend to be ignored). The dependable combination for a vocal-free track:

1. Toggle **Instrumental** on in Custom Mode
2. Add `[Instrumental]` in the Lyrics field (or `[Instrumental Break]` for a vocal-free section inside a song with vocals)
3. Put `vocals` in the official **Exclude** field under Advanced Options

See [Instrumental Mode](#instrumental-mode) for prompt patterns that work without vocals.

### How metatags work

Metatags are processed as arrangement directives, not as lyrics. When Suno encounters `[Chorus]`, it: 1. Signals a section change in the arrangement 2. Applies typical chorus characteristics (melodic emphasis, fuller instrumentation, higher energy) 3. If the same `[Chorus]` text appears again, attempts to repeat the melody and arrangement

Metatags are case-insensitive: `[VERSE]`, `[Verse]`, and `[verse]` are equivalent.

**Why metatags matter more than prompt text:** Without metatags, Suno infers song structure from line breaks and lyric content. The model guesses where a verse ends and a chorus begins based on training patterns. Metatags remove the guesswork. Instead of hoping Suno recognizes your chorus as a chorus, `[Chorus]` explicitly triggers chorus-appropriate musical behavior: melodic hooks, fuller instrumentation, higher energy, and repetition on subsequent occurrences. The effect compounds over a full song. A 3-minute track with no metatags has maybe 6–8 structural decisions made by Suno’s inference. A track with metatags has 6–8 structural decisions made by you.

### Tag behavior in V5.5

The meta tag vocabulary is unchanged through V5.5: the March 2026 release added Voices, Custom Models, and My Taste, but no new tags and no changes to tag processing. Four V5.5-era specifics worth knowing:

* **Exclude field over negative tags.** Negative instructions in the Style field (“no drums”) are unreliable; the Exclude field under Advanced Options is the official control for unwanted instruments and elements.
* **Structure labels in the web Lyrics Editor are the same control on a different surface.** The July 2026 [Lyrics Editor](#the-web-lyrics-editor-july-2026) lets you label sections Verse, Chorus, or Outro from the UI to tell the model how the track should flow — the same job `[Verse]`/`[Chorus]`/`[Outro]` bracket tags do in a plain-text lyric sheet. Use labels when writing inside the editor, bracket tags when preparing lyric sheets outside Suno to paste in; the tag vocabulary itself is unchanged.[40](#fn:41)
* **My Taste does not override your tags.** My Taste biases defaults when prompts are underspecified; explicit Style field descriptors still override its preferences, and Lyrics-field meta tags still set the structure. The magic wand icon (Style Augmentation) generates personalized style text, not structural tags.
* **Time signature is an editing surface, not a generation tag.** 3/4, 6/8, and odd time signatures are supported in the Studio grid and metronome, but the setting does not condition the generative model itself.

---

## Structural Tags

These tags define song sections and control arrangement flow.

### Primary structural tags

| Tag | Purpose | Musical Effect |
| --- | --- | --- |
| `[Intro]` | Opening section | Usually instrumental or sparse, sets the tone |
| `[Verse]` or `[Verse 1]` | Verse section | Moderate energy, narrative focus, varied melody |
| `[Pre-Chorus]` | Builds to chorus | Rising energy, transitional harmony |
| `[Chorus]` | Hook/refrain | Peak energy, memorable melody, full instrumentation |
| `[Post-Chorus]` | After chorus | Maintains energy, transitions back down |
| `[Bridge]` | Contrasting section | Different chords, different energy, provides variety |
| `[Breakdown]` | Stripped-back section | Reduced instrumentation, creates space |
| `[Build]` or `[Build-Up]` | Energy ramp | Progressive intensity increase, common in EDM |
| `[Drop]` | High-energy payoff | Maximum instrumentation and energy, follows a build |
| `[Hook]` | Catchy phrase | Short, memorable musical phrase |
| `[Interlude]` | Instrumental break | Connects sections, palette cleanser |
| `[Outro]` | Closing section | Winds down energy, brings closure |
| `[End]` | Hard stop | Signals the song should end (prevents trailing audio) |

### Numbered sections

Use numbers to distinguish repeated section types:

```
[Verse 1] First verse lyrics here[Chorus] Chorus lyrics[Verse 2] Second verse with different lyrics[Chorus]Same chorus lyrics (encourages melodic repetition)
```

Numbering verses helps Suno understand that each verse should have different melody while choruses should repeat their melody.

---

## Instrumental and Vocal Tags

These tags control instrumentation and vocal behavior within sections.

### Instrumental tags

| Tag | Effect |
| --- | --- |
| `[Instrumental]` | Section with no vocals |
| `[Instrumental Intro]` | Instrumental opening |
| `[Instrumental Break]` | Mid-song instrumental section |
| `[Guitar Solo]` | Guitar-focused instrumental passage |
| `[Piano Solo]` | Piano-focused passage |
| `[Drum Solo]` | Percussion-focused passage |
| `[Bass Solo]` | Bass-focused passage |
| `[Saxophone Solo]` | Sax-focused passage |
| `[Strings Rise]` | String section swell |
| `[Percussion Break]` | Rhythm-focused breakdown |
| `[Synth Solo]` | Synthesizer lead passage |

### Vocal tags

| Tag | Effect |
| --- | --- |
| `[Male Vocal]` | Switches to male vocal |
| `[Female Vocal]` | Switches to female vocal |
| `[Duet]` | Two vocal parts |
| `[Choir]` | Choral vocals |
| `[Harmony]` | Vocal harmonies |
| `[Rap]` | Rap delivery |
| `[Spoken Word]` | Spoken delivery, not sung |
| `[Whisper]` | Whispered delivery |
| `[Scream]` | Screamed/shouted delivery (metal, punk) |
| `[Ad-lib]` | Improvised vocal phrases |
| `[Humming]` | Hummed melody |
| `[Backing Vocals]` | Background vocal parts |

---

## Advanced Metatag Patterns

### Parameterized metatags

Metatags accept descriptive modifiers after a colon:

```
[Verse: whispered vocals, acoustic guitar only] Walking through the morning mistThe world still sleeping, still[Chorus: full band, powerful vocals]But I'm awake, I'm alive And every sound is a sign
```

The colon syntax lets you modify individual sections without changing the global Style field. Parameterized metatags are the most powerful metatag feature, giving you per-section control over arrangement.

### Dynamic and production metatags

| Tag | Effect |
| --- | --- |
| `[Fade In]` | Gradual volume increase |
| `[Fade Out]` | Gradual volume decrease |
| `[Silence]` | Brief pause in the audio |
| `[Crescendo]` | Building intensity |
| `[Decrescendo]` | Decreasing intensity |
| `[Tempo: slow]` | Section-level tempo shift |
| `[Key Change]` | Harmonic modulation |

### Combining structural and modifier tags

```
[Intro: ambient pads, reversed guitar, ethereal][Verse 1: lo-fi drums, muted bass, whispered vocals] Words that float on morning air Disappearing into light[Pre-Chorus: building energy, adding layers] But something shifts beneath the surface[Chorus: full production, soaring vocals, epic drums] We break through the silence Into the wide open sky[Bridge: stripped down, piano only, vulnerable vocals] And in the quiet after the storm[Outro: fade out, ambient reprise]
```

The result is DAW-level arrangement control through text alone.

---

## Creative Sliders

Creative Sliders are V4.5+ controls that shape the generation’s personality. They appear in Custom Mode below the Lyrics field.[11](#fn:11)

**Why sliders exist alongside text prompts:** Text prompts define *what* to generate (genre, instruments, mood). Sliders control *how* the model interprets those prompts. A “jazz” prompt at low Weirdness produces a conventional jazz standard. The same prompt at high Weirdness produces jazz that breaks its own conventions. The prompt defines the vocabulary; the sliders define the grammar.

### Weirdness

**Range:** Safe ← → Chaos (slider, no numerical values exposed)

| Position | Effect |
| --- | --- |
| **Safe (left)** | Conventional structure, predictable genre adherence, safe melodic choices |
| **Center (default, ~50%)** | Balanced. Some creative surprises within genre conventions |
| **Chaos (right)** | Unconventional structures, unexpected harmonic choices, genre-bending. Higher risk of incoherence |

**How Weirdness behaves in practice:** at low values, Suno picks the most probable next musical event at each step, producing conventional results; at high values, lower-probability events appear more often, producing surprising combinations. Suno does not document the specific mechanism, but the observable tradeoff is coherence: safer settings sound more polished, weirder settings produce more creative but potentially less coherent output.

**When to increase Weirdness:** - Experimental or avant-garde genres - When conventional results feel generic - For genre-blending experiments

**When to decrease Weirdness:** - Commercial music that needs to sound “normal” - When working within strict genre conventions - For background/ambient music that shouldn’t draw attention to itself

### Style Influence

**Range:** Loose ← → Strong (slider)

| Position | Effect |
| --- | --- |
| **Loose (left)** | Style descriptors are suggestions, not mandates. Suno takes more creative liberty |
| **Center (default)** | Balanced adherence to style descriptors |
| **Strong (right)** | Strict adherence to style descriptors. Less creative deviation |

**Use Strong** when your Style field is precise and you want exactly what you described. **Use Loose** when you want Suno to interpret your prompt more freely and potentially surprise you.

### Audio Influence

**Range:** Controls how much any uploaded audio reference affects generation.

Available when using Audio Upload (Covers, Remixes, or Add Vocals/Instrumentals). Higher values make the output more closely follow the reference audio’s characteristics.

---

## Song Editor

The Song Editor enables post-generation editing without re-creating the entire song. The Song Editor solves the “90% perfect but one section is wrong” problem.[12](#fn:12)

### Available operations

| Operation | What It Does | When to Use |
| --- | --- | --- |
| **Inpainting** | Replace a specific time range with new content | A verse is weak but the chorus is perfect |
| **Extend** | Continue the song beyond its current endpoint | Song ends too soon or needs another section |
| **Crop** | Trim the song to a shorter length | Remove trailing silence or unwanted sections |
| **Fade In/Out** | Apply gradual volume changes at start/end | Professional intro/outro polish |
| **Replace Section** | Regenerate a section with new instructions | A bridge doesn’t work tonally |

### Inpainting workflow

1. Select the time range to replace (drag on the waveform)
2. Optionally provide new lyrics/metatags for the replacement section
3. Generate: Suno creates new content that matches the surrounding audio
4. Listen and compare. Accept or regenerate.

> **Inpainting is iterative.** Rarely does the first replacement perfectly match the surrounding context. Budget 2–5 attempts for clean transitions into the surrounding material.

### Extend workflow

1. Click Extend on any existing generation
2. Optionally provide lyrics/metatags for the continuation
3. Suno generates ~30–60 seconds of new audio that continues from the endpoint
4. Each extension is a separate generation (costs credits)

**Best practice:** Include a structural metatag at the start of your extension prompt (e.g., `[Chorus]` or `[Outro]`) to guide what the extension generates.

---

## Covers and Remixes

Pro and Premier tiers can create covers and remixes of existing Suno tracks.

### Covers

Upload or select an existing Suno track as a reference, then apply a new style:

The cover maintains the melody and lyrics but reimagines the arrangement and production.

### Remixes

Remixes take an existing track and rework it more aggressively than covers:

### Add Vocals / Add Instrumentals

Two specialized modes that layer onto existing audio:

* **Add Vocals**: Upload an instrumental track, Suno generates vocals over it
* **Add Instrumentals**: Upload a vocal track, Suno generates instrumentation behind it

Both modes integrate Suno into traditional production workflows: record real vocals and let Suno generate the backing track, or vice versa.

---

## Voices

The Voices system (Pro/Premier, v5.5) lets you create and reuse consistent vocal characters across generations. Instead of hoping each generation assigns a similar voice, you define a voice and reference it. Voices builds on the earlier Personas work; Suno’s current help center says the Create menu now uses **Voices**, while Style Personas remain inside the Voices menu.[15](#fn:15)[31](#fn:31)

### Creating a Persona Voice

1. Generate a song with vocals you like
2. Click the three-dot menu on that generation and select “Create Persona”
3. Name the persona descriptively (e.g., “Warm Alto Folk”, “Raspy Baritone Rock”, “Ethereal Soprano”)
4. The persona is saved to your account library

**Tips for creating effective personas:** - Generate specifically for the persona, not as a side effect of another song. Use a clear, genre-appropriate Style prompt with prominent vocals. - Avoid creating personas from songs with heavy vocal processing (auto-tune, distortion). The persona captures the processed sound, not the underlying voice. - Create genre-specific personas rather than one “universal” voice. A persona trained on an indie folk track produces unpredictable results on a trap beat.

### Using Persona Voices

In Custom Mode, select your saved persona from the Persona dropdown before generating. The persona applies to all generations in that session until you change it.

**Persona behavior:** - The persona preserves **timbre** (vocal tone, resonance) and **basic delivery style** (breathy, raspy, smooth) - It does **not** preserve exact melodic patterns, phrasing, or rhythmic delivery. Those come from the Style prompt and metatags - Applying a persona across different tempos and keys works well. Applying across vastly different genres (e.g., jazz persona on death metal) produces inconsistent results.

### Persona management

* **Storage limit**: Suno allows saving multiple personas (the exact limit is not publicly documented, but users report 20+ without issues)
* **Naming convention**: Use descriptive names that include vocal quality and genre context. You’ll forget which “Voice 3” was
* **Deletion**: Personas can be deleted from your library. Deletion is non-reversible.
* **Account-specific**: Personas cannot be shared between accounts or exported

### Limitations

* Persona Voices capture timbre and basic delivery style, not exact vocal technique
* Results vary when applying a persona far outside its original genre
* Persona Voices are account-specific and cannot be shared
* The December 2025 update improved persona consistency across generations, but perfect reproduction is still not guaranteed[15](#fn:15)

### Voice Cloning (V5.5)

V5.5 introduced Voices, allowing Pro and Premier subscribers to clone their own voice for use in generations.[30](#fn:30)[31](#fn:31) Unlike Persona Voices (which extract timbre from a generated song), a verified Voice captures the characteristics of a real human voice.

**How it works:**

1. Record or upload a vocal sample
2. Complete a verification process that compares a spoken phrase against your uploaded or live-captured vocal sample
3. The cloned voice becomes available as a selectable voice in Custom Mode

**Key differences from Persona Voices:**

| Aspect | Persona Voices | Voice Cloning |
| --- | --- | --- |
| **Source** | Generated Suno song | Real human voice recording |
| **Verification** | None | Identity verification required |
| **Fidelity** | Captures timbre and basic delivery | Higher-fidelity reproduction of the source voice |
| **Availability** | Pro/Premier | Pro/Premier, v5.5 only; restricted by age/location |

**Verification and sharing:** Suno requires verification to prevent unauthorized cloning of other people’s voices. You must confirm that you are the owner of, or have explicit permission to use, the voice being cloned. Only you can create with your Voice, but songs that feature your Voice can be covered or remixed by other users if you publish or share the song and allow remixing in the publish options.[31](#fn:31)

### Custom Models (V5.5)

Custom Models let Pro and Premier subscribers personalize V5.5 to their specific music style.[30](#fn:30)[31](#fn:31) Rather than starting from Suno’s general-purpose model each time, a Custom Model is tuned to your creative preferences.

**How Custom Models work:**

1. Upload at least six songs from your catalog or tracks made outside Suno that represent your desired style
2. Keep the training material stylistically consistent, mixing random genres in one model makes the learning noisy; sticking to a single lane (e.g., full orchestral, future bass, indie folk) gives the model a clearer direction
3. Name the Custom Model and Suno trains a personalized version of V5.5 based on those selections
4. Use the Custom Model for future generations that inherit your style fingerprint

**Limits:** Up to 3 Custom Models per Pro or Premier subscriber. This allows maintaining separate models for different projects or genres (e.g., one for indie folk, one for electronic, one for hip-hop).

**What Custom Models capture:** Genre tendencies, arrangement patterns, production aesthetic, and stylistic preferences from your selected training songs. They do not memorize or reproduce specific melodies or lyrics from training material.

---

## My Taste (V5.5)

My Taste is a V5.5 feature available to all users (including free tier) that adapts Suno’s generation behavior to individual preferences over time.[30](#fn:30)[31](#fn:31)

**How it works:** As you generate, like, and interact with songs, Suno builds a preference profile. My Taste is enabled by default but can be viewed, edited, or disabled from the avatar menu. The magic wand icon at the top right of the Styles box is the primary trigger: with Style Augmentation enabled, it generates a style text tailored to your taste profile.[31](#fn:31) My Taste influences generation defaults, subtle biases toward the genres, production styles, vocal qualities, and structural patterns you’ve consistently favored.

**What My Taste affects:** - Default genre and style tendencies when prompts are underspecified - Production aesthetic preferences (lo-fi vs. polished, sparse vs. dense) - Vocal style biases - Arrangement and structural patterns

**What My Taste does not replace:** - Explicit Style field descriptors still override My Taste preferences - Creative Sliders still function independently - Persona Voices and Voice Cloning are unaffected

**Practical implication:** My Taste reduces the “cold start” problem where new users get generic results. Over time, even a simple prompt like “upbeat rock song” will produce results that align more closely with the specific flavor of rock you prefer, based on your generation history.

---

## The Generation Loop

Effective Suno usage follows an iterative workflow, not a single-prompt approach.

### The production cycle

```
1.  IDEATION  ↓  Generate  5 - 10  variations  with  different  Style  descriptors  ↓  (Cost:  ~ 25 - 50  credits)2.  SELECTION  ↓  Pick  the  1 - 2  best  results  ↓  Identify  what  works  and  what  doesn 't3.  REFINEMENT  ↓  Adjust  Style  descriptors  based  on  what  you  heard  ↓  Refine  lyrics  and  metatags  ↓  Regenerate  with  tighter  prompts  ↓  (Cost:  ~ 15 - 30  credits  per  round)4.  EXTENSION  ↓  Extend  the  best  track  to  full  length  ↓  Add  missing  sections  (bridge,  outro)  ↓  (Cost:  ~ 5 - 15  credits)5.  EDITING  ↓  Use  Song  Editor  to  fix  weak  sections  ↓  Inpaint,  crop,  fade  as  needed  ↓  (Cost:  ~ 5 - 20  credits)6.  EXPORT  ↓  Download  final  audio  (MP3/ WAV)  ↓  Optionally  export  stems  for  DAW  work
```

**Typical cost for a polished track:** 50–100 credits (roughly 10–20 generated songs, usually 5–10 two-song Create batches plus edits).

### Walkthrough: one song from concept to export

Here is a complete production cycle for a single track, showing actual prompts and decisions at each stage:

**1. Concept:** “Moody indie folk song about insomnia.”

**2. First Create batch (10 credits, 2 variations):**

```
 Style:  Indie  folk,  slow  tempo,  acoustic  guitar  fingerpicking,  soft  female  vocals,  intimate  lo - fi  recording,  melancholic Lyrics:[Verse 1] The  ceiling  holds  no  answers Just  shadows  and  the  clock Every  hour  stretches  longer When  the  world  has  gone  to  dark[Chorus] Sleep  won't come, sleep won' t  come I 'm counting every sound[Verse 2] The neighbors'  lights  went  out  at  ten The  street  grew  still  by  twelve Now  it 's somewhere past forever And I' m  talking  to  myself[Chorus] Sleep  won't come, sleep won' t  come I ' m  counting  every  sound[Outro: fade out, humming]
```

**3. Selection:** Variation B has the right vocal tone but the chorus melody is too upbeat for the mood. Variation A has a better chorus but thin guitar tone.

**4. Refinement (10 credits):** Re-generate with adjusted Style: changed “lo-fi recording” to “warm analog recording” and added “sparse arrangement.” Kept the same lyrics. New Variation A has the warmth from the first round and a subdued chorus.

**5. Extension (5 credits):** The song ends at 2:30. Extended with `[Bridge: piano only, vulnerable vocals]` + new lyrics + `[Chorus]` + `[Outro: fade out, ambient reprise]`. The bridge introduces piano naturally.

**6. Editing (10 credits):** The transition from verse 2 into the chorus is abrupt. Used Song Editor to inpaint a 4-second window at that junction. Second inpainting attempt matches smoothly.

**7. Export:** Downloaded WAV for mastering in Logic Pro. Total cost: 35 credits, roughly 7 song-level generations or edits.

The key insight: most credits went to the first two rounds (finding the right sound), not to the last three (refining a good take). Front-loading prompt precision saved at least 30 credits compared to vague-prompt-and-iterate approaches.

### Credit-efficient workflow tips

1. **Spend time on the prompt, not on generations.** A well-crafted Style + Lyrics prompt produces better first results than rapid iteration with vague prompts.
2. **Generate in batches.** When exploring a concept, generate 4–6 variations at once, then pick the best direction before refining.
3. **Use the Song Editor over regeneration.** If 80% of a track is good, edit the remaining 20% rather than regenerating the entire song.
4. **Save successful Style prompts.** When a particular descriptor combination works well, save it for reuse.

---

## Suno Studio DAW

Suno Studio (Premier tier, launched with V5) is an in-browser digital audio workstation for post-generation editing. It bridges the gap between Suno’s generation engine and traditional music production.[2](#fn:2)

### Studio capabilities

| Feature | What It Does |
| --- | --- |
| **Multi-track view** | Visual timeline with individual stem tracks |
| **Mix controls** | Per-stem volume, pan, mute, solo |
| **Warp markers** | Time-stretch specific sections without affecting pitch |
| **Remove FX** | Strip reverb, delay, and other effects from stems |
| **Alt takes** | Generate alternative versions of specific sections |
| **Time signatures** | Adjust or correct time signature interpretation |
| **Stem isolation** | Access up to 12 individual stems for detailed mixing |

### Studio 1.2 (February 2026)

The latest Studio update added:[25](#fn:25)

* **Warp markers with quantize**: Micro-adjust timing of individual notes and phrases, with snap-to-grid quantization for tighter rhythmic alignment
* **Remove FX**: Strip AI-applied reverb and delay to get dry stems
* **Alt takes**: Generate and audition alternative sections inline
* **Time signature support in the Studio grid**: 3/4, 6/8, and odd time signatures are supported in the grid and metronome for editing and alignment. Time signature does **not yet** condition the generative model itself; the tag/advanced setting affects editing surfaces, not generation behavior.[4](#fn:4)

Suno’s Sounds (browse and layer pre-made audio elements) is a separate beta feature in Create Mode, not a Studio 1.2 feature. Personas are documented separately; check the in-app UI and the official help center for the current surface on both.

### WavTool acquisition

Suno acquired WavTool, a browser-based DAW with VST plugin support, sample-accurate editing, and AI-powered features, in June 2025.[27](#fn:27) WavTool’s core team joined Suno in product and engineering leadership roles. The acquisition explains Studio’s rapid feature development: Warp Markers, Remove FX, and the Sounds library reflect WavTool’s professional DAW capabilities integrated into Suno’s generation-first workflow. CEO Mikey Shulman framed the move as empowering musicians with “tools that amplify human creativity.”[27](#fn:27)

### MILO-1080: AI Step Sequencer

In March 2026, Suno launched **MILO-1080** (Model-Integrated Loop Orchestrator), a 16-track step sequencer and synth designer aimed at experienced producers and beatmakers.[28](#fn:28) MILO-1080 combines manual sequencing with AI-generated sounds:

* **Text-to-sound generation**: Create samples from text prompts
* **Suno track library**: Pull clips from previously generated Suno tracks
* **Built-in synth engine**: Design sounds manually without AI
* **MIDI support**: Standard MIDI input/output for hardware integration
* **16 tracks**: Full multi-track sequencing with per-track controls

MILO-1080 represents Suno’s push beyond text-to-music toward becoming a full creative platform. Combined with the WavTool acquisition and Studio DAW, it signals that Suno is targeting professional producers, not just casual users.

### Should you use Studio or export to a DAW?

| Scenario | Use Studio | Export to DAW |
| --- | --- | --- |
| Quick fixes (volume balance, muting a stem) | Yes | No |
| Full professional mixing and mastering | No | Yes |
| Trying arrangement variations | Yes | No |
| Adding external audio (live instruments, vocals) | No | Yes |
| Casual listening and sharing | Yes | No |
| Commercial release preparation | Possibly | Yes |

---

## Stem Separation and Export

Suno offers three stem separation methods, overhauled on June 11, 2026 for cleaner, crisper, artifact-free output:[37](#fn:38)

### Split from Mix (2 stems, all tiers)

Pull *any* single instrument or voice out of the mix and get two stems: the targeted instrument or voice, and everything else. This generalizes the older vocals-vs-instrumental split — the target no longer has to be the vocal.

Useful for: karaoke versions, vocal sampling, isolating a single instrument, basic remixing.

### Auto Split (12 categories, Pro/Premier)

Suno’s classic model, splitting a song into up to 12 stem categories:[22](#fn:22) - Vocals, drums, bass, guitar, keys/piano, synths, strings, brass, woodwinds, percussion, effects, other

### Advanced Split (Premier)

Choose exactly what to extract from a list of nearly 100 instruments, producing a custom set of stems tuned to the track. Premier-only.[37](#fn:38)

**An important distinction:** Suno’s “stem separation” is fundamentally different from tools like iZotope RX or Demucs. Those tools analyze a mixed audio file and attempt to isolate sources after the fact. Suno likely exports the individual generation layers directly, since it created all the audio in the first place. The result is closer to exporting submixes from a DAW than to post-hoc source separation.[23](#fn:23) In practice, Suno stems are cleaner than what third-party separation tools produce on the same mixed file, but they may not null-test perfectly against the original mix.

**Quality notes:** Expect some bleed between stems, especially between similar-frequency instruments. The separation quality improved significantly in V5. For professional work on arbitrary audio files (not Suno-generated), purpose-built tools like Demucs and iZotope RX remain the standard.[23](#fn:23)

### Export formats

* **MP3**: Standard compressed audio. Good for sharing, streaming, and drafts.
* **WAV**: Uncompressed audio. Required for professional DAW work and mastering.

---

## DAW Integration

Suno’s output integrates into traditional production workflows via stem export.

### Recommended workflow

1. **Generate in Suno** until the arrangement and vibe are right
2. **Export 12 stems** (Pro/Premier) as WAV files
3. **Import into your DAW** (Logic Pro, Ableton, Pro Tools, FL Studio, Reaper)
4. **Mix and master** with professional tools and processing
5. **Replace or augment** individual stems with live recordings if needed

### What you gain from DAW mixing

* **EQ and compression**: Per-stem tonal shaping that Suno’s AI mixing doesn’t provide
* **Spatial processing**: Precise stereo placement, reverb sends, delay throws
* **Automation**: Dynamic changes over time (fade builds, filter sweeps)
* **External instruments**: Layer live recordings with AI-generated stems
* **Mastering chain**: Loudness normalization, limiting, final polish for release
* **Automation scripts**: Use [Claude Code](/guides/claude-code) to build prompt templates, batch-process Style field variations, or script the generation-selection-refinement loop

---

## Genre Blending

One of Suno’s unique strengths is generating music at genre intersections that would require multiple specialist musicians in traditional production.

### Effective blending patterns

**Two-genre fusion (most reliable):**

**Genre + era mashup:**

```
 80 s  synthwave  meets  modern  trap,  analog  synths,  808  bass,  retro - futuristic
```

**Genre + unexpected instrument:**

### Blending rules

1. **Lead with the dominant genre.** “Jazz with electronic elements” produces different results than “Electronic with jazz elements.”
2. **Limit to 2–3 genres.** More than that and Suno’s output becomes an unfocused compromise.
3. **Use era markers to anchor style.** “90s” or “2020s” helps Suno pick the right production conventions.
4. **Increase Weirdness** for unusual fusions. The default Weirdness setting tries to normalize everything, which defeats the purpose of genre blending.

---

## Multi-Section Composition

For songs longer than 8 minutes, you need to compose in multiple generations and join them.

### Strategy 1: Extend

Generate the first section, then use Extend to add subsequent sections. Each extension uses the ending of the previous section as context.

**Pros:** Musical continuity. Each extension naturally follows the previous. **Cons:** Less control over later sections. Musical drift over multiple extensions.

### Strategy 2: Section-by-section generation

Generate each section independently with specific metatag + Style combinations, then join in a DAW.

**Pros:** Maximum control over each section’s character. **Cons:** Transitions between independently generated sections can sound jarring. Requires DAW skills for joining.

### Strategy 3: Hybrid approach (recommended)

1. Generate the core of the song (verse-chorus-verse-chorus) as one generation
2. Extend for the bridge and final chorus
3. Use Song Editor to inpaint any weak transitions
4. Export stems and finalize in a DAW

---

## Prompt Chaining

Build complex songs through a sequence of related generations.

### Chain pattern

```
 Generation  1  "Atmospheric intro, ambient pads, slow build"   Extend  with  "[Build-Up] [Drop: full energy, heavy drums]"   Extend  with  "[Verse 1: vocals enter, riding the beat]"   Extend  with  "[Chorus: anthemic, crowd-singing energy]"   Extend  with  "[Outro: fade out, return to ambient pads]"
```

Each extension inherits the musical DNA of the previous generation, creating a coherent multi-section composition without starting from scratch each time.

---

## Troubleshooting

### Why does my Suno song sound wrong?

| Problem | Likely Cause | Solution |
| --- | --- | --- |
| Song sounds nothing like the Style prompt | Competing descriptors, or Weirdness too high | Reduce to 4–5 core descriptors. Lower Weirdness. |
| Vocals sound robotic | V4.5-All model on free tier | Upgrade to Pro for V5 vocal quality. |
| Song ends abruptly | No `[Outro]` tag | Add `[Outro]` or `[End]` to lyrics. |
| Song keeps going after natural ending | Suno filling to max length | Add `[End]` tag after your final section. |
| Wrong genre is dominant | Genre listed second is being deprioritized | Put your primary genre first in the Style field. |
| Metatags appear as lyrics | Syntax error in tag | Check for typos. Tags must be `[Tag]` with square brackets. |
| Inconsistent vocals across sections | No Persona Voice set | Use Persona Voices for consistency across generations. |
| Extension doesn’t match original | Too many generations between original and extension | Extend from the most recent version, not the original. |
| Instrumental track has vocal artifacts | Style descriptors imply vocals | Explicitly toggle Instrumental mode. Add `[Instrumental]` tag. |

### Generation quality checklist

Before spending credits on refinement, verify your prompt covers:

* [ ] **Genre is specific** (not just “rock” but “indie rock” or “post-punk”)
* [ ] **Vocal style is described** (or Instrumental is toggled on)
* [ ] **Metatags define structure** (at minimum: Verse, Chorus, Outro)
* [ ] **4–7 descriptors** in the Style field (not too few, not too many)
* [ ] **Mood is explicit** (Suno defaults to upbeat/positive without guidance)

---

## Commercial Licensing

> **Verified as of May 2026.** Licensing terms change. Check Suno’s current Terms of Service for binding language.[5](#fn:5)

### What each tier allows

| Usage | Free | Pro | Premier |
| --- | --- | --- | --- |
| Personal listening | Yes | Yes | Yes |
| Social media posts | Non-monetized only | Yes | Yes |
| Monetized YouTube/TikTok | No | Yes | Yes |
| Streaming platforms (Spotify, Apple Music) | No | Yes | Yes |
| Commercial products (ads, games, film) | No | Yes | Yes |
| Royalty obligations to Suno | N/A | None (100% yours) | None (100% yours) |

### Important caveats

**Copyright protection for 100% AI content is legally unsettled.** Suno’s current help center treats paid-plan outputs as **owned by the subscriber** for platform and commercial-use purposes: the songs are yours to use, monetize, and distribute on the terms of your plan.[26](#fn:26) What is not guaranteed is formal copyright protection under local law. The US Copyright Office has stated that purely AI-generated works cannot be copyrighted absent sufficient human authorship, so the ownership Suno grants on its platform does not automatically translate into a legally enforceable copyright claim. The implications: - You have commercial **use** rights (Suno grants you ownership on a paid plan) - But the work may not qualify for **copyright registration** without human authorship elements - You may not be able to prevent others from using the same or similar output - Adding human creative elements (original lyrics, live instrument recordings, arrangement choices in a DAW) strengthens your copyright claim - **No retroactive licensing:** Starting a paid subscription after creating a song on the free tier does not grant retroactive commercial rights to that song[34](#fn:34) - **No consumer-plan indemnification promise:** Suno’s current pricing and rights pages do not advertise indemnification for Pro or Premier users. If a Suno-generated song is claimed to infringe existing copyrighted music, do not assume a consumer subscription includes legal defense or reimbursement.[5](#fn:5)[13](#fn:13)[26](#fn:26)

**Revenue is yours.** Pro and Premier users keep 100% of revenue from Suno-generated music. Suno does not claim royalties or revenue share.[5](#fn:5)

---

## Copyright and Legal Landscape

AI music generation exists in an evolving legal environment.

### Key legal developments

* **Warner Music partnership (November 2025)**: Warner settled its lawsuit against Suno and announced a strategic partnership. Suno acquired Songkick and will develop WMG-licensed models for release in 2026, with current unlicensed models being phased out.[34](#fn:34) The partnership announcement described a future where free users would lose audio downloads and paid users would face download caps with purchasable top-ups; as of May 2026 those caps have **not shipped** in Suno’s official help center. Suno still documents MP3 downloads for free users, with WAV restricted to paid plans. Treat the download-cap language as announced-but-unshipped until Suno publishes the rollout. Artists and songwriters who opt in will gain access to revenue opportunities in AI-generated music. Artists retain control over name, image, likeness, and voice usage.[6](#fn:6)[35](#fn:36)
* **UMG and Sony lawsuits**: Major label lawsuits against Suno remain active. Dispositive motions in UMG Recordings v. Suno are now due **April 9, 2027** — Judge Saylor granted a joint motion to amend the schedule on June 30, 2026, moving the deadline from the January 8, 2027 date widely reported earlier. The amended schedule runs document production to July 30, 2026, fact discovery and depositions to September 30, expert disclosure to November 18, and expert depositions to March 5, 2027.[32](#fn:32) In March 2026, UMG’s EVP and Chief Digital Officer Michael Nash publicly stated that “we are seeing no indication that AI royalty dilution is a material issue for UMG from a revenue perspective”, directly contradicting UMG’s court filings claiming the market would be “overrun” by Suno-generated works.[33](#fn:33) Claims center on alleged use of copyrighted recordings in training data.[6](#fn:6)
* **Source-code leak and data breach (July 2026)**: A hacker leaked 2023–24 Suno source code that documents large-scale training scraping — YouTube Music (over 2 million clips, ~113,879 hours), Pond5, IMSLP, Genius, Deezer, Jamendo, Freesound, MuseScore, and podcasts via RSS — substantiating the stream-ripping allegations at the center of the label litigation.[42](#fn:43) The same incident exposed account data for 55.3 million users (emails, names, phone numbers, physical addresses, purchase records, partial card data), verified by Have I Been Pwned on July 20, 2026; the breach itself dates to November 2025 via a compromised employee credential, and Suno has said it does not plan individual notifications.[43](#fn:44) If you have a Suno account, treat the credential exposure as real: rotate your password and watch for phishing referencing your Suno purchase history.
* **GEMA lawsuit (Germany)**: German performance rights organization GEMA filed suit against Suno in Munich. The first hearing was held March 9, 2026; the Munich Regional Court originally scheduled its decision for June 12, 2026, then **postponed the ruling to July 31, 2026** for internal court reasons (“aus dienstlichen Gründen”). A ruling for GEMA would be the first major European decision holding that AI platforms need authorization to train on copyrighted music.[29](#fn:29)[38](#fn:39)
* **Spark incubator program (June 25, 2026)**: Suno launched **Spark**, an incubator for unsigned artists 18+ — grants from the low thousands to tens of thousands of dollars, marketing funds, songwriting-camp invitations, and feedback, running through at least March 2027. Participants retain creative and commercial rights and choose their distributor. **Read the fine print:** reporting on the participation agreement highlights a perpetual non-disparagement clause (never say anything negative about Suno) and a 60-day exclusivity window against rival AI-music tools after the last sponsored post — breaking either is a material breach.[39](#fn:40)
* **Udio/UMG settlement (2025)**: Competitor Udio settled with UMG, establishing some precedent for the industry.[7](#fn:7)
* **US Copyright Office**: Has stated that purely AI-generated works cannot be copyrighted, though works with sufficient human authorship containing AI elements may qualify.[8](#fn:8)

### Practical guidance

1. **Don’t use Suno to replicate specific copyrighted songs.** The Covers feature is designed for covering Suno-generated tracks, not commercial recordings.
2. **Add human creative elements** to strengthen copyright claims: write original lyrics, record live instruments over Suno stems, make arrangement decisions in a DAW.
3. **Document your creative process.** If your work is ever challenged, evidence of human creative choices strengthens your position. Tools like [Obsidian](/guides/obsidian) can serve as timestamped creative journals for this purpose.
4. **Stay current on legal developments.** This area is changing rapidly.

---

## Competitors and Alternatives

| Platform | Strengths | Weaknesses | Best For |
| --- | --- | --- | --- |
| **Suno** | Best overall song quality, extensive editing tools, Studio DAW | No official API, non-deterministic, credits don’t roll over | Complete song production |
| **Udio** | Best stem quality (48kHz native), strong genre accuracy | Smaller user base, fewer editing tools | Stem-based production |
| **Stable Audio** | Official API, SFX/sound design capability, open weights | Weaker vocal quality, shorter outputs | API integration, sound effects |
| **Google MusicFX** | Free, accessible | Limited control, shorter outputs, no commercial use | Casual experimentation |
| **AIVA** | Classical/film score focus, MIDI export | Narrow genre range | Film and game scoring |

### Which AI music generator should you use?

* **Full songs with vocals**: Suno (V5.5)
* **Stems for DAW production**: Udio (highest stem quality)
* **API-driven generation**: Stable Audio (public API option in this comparison set)
* **Sound design and SFX**: Stable Audio
* **Film scoring**: AIVA (MIDI export for orchestral editing)
* **AI image generation for album art**: See the [Midjourney guide](/guides/midjourney) for prompt engineering techniques that pair well with music production workflows

---

## API and Integration Status

> **Verified as of May 2026.**

**Suno does not publish an official public developer API in its current docs or pricing pages.** I found no official REST API or SDK documentation for individual users or developers in this pass. Treat reverse-engineered wrappers as unofficial and brittle.[13](#fn:13)[17](#fn:17)

### What exists

| Access Type | Status | Details |
| --- | --- | --- |
| **Official public API** | Not available | No announced timeline |
| **Enterprise/partner API** | Not publicly documented | Contact Suno directly rather than assuming consumer-plan API access. |
| **Community wrappers** | Unofficial | [gcui-art/suno-api](https://github.com/gcui-art/suno-api), a reverse-engineered wrapper. Not endorsed by Suno. May break without notice.[9](#fn:9) |
| **Chirp API** | Historical | Early API access program. No longer accepting new users. |

### For developers

If you need programmatic music generation: - **Stable Audio**: Has an official API with documented endpoints - **Replicate**: Hosts open-source music generation models with API access - **Custom deployment**: Open-source models like MusicGen (Meta) can be self-hosted

---

## Quick Reference Card

### Custom Mode template

```
 STYLE  FIELD:[Genre]  [Subgenre],  [Tempo],  [Key  instruments],  [Vocal  style],  [Production],  [Mood] LYRICS  FIELD:[Intro:  descriptors][Verse  1] Your  lyrics  here[Pre - Chorus] Building  lyrics[Chorus] Hook  lyrics[Verse  2] More  lyrics[Chorus] Same  hook  (for  melodic  repetition)[Bridge:  contrasting  descriptors] Different  energy  lyrics[Chorus] Final  hook[Outro:  fade  out]
```

### Essential metatags

| Tag | Purpose |
| --- | --- |
| `[Verse]` | Narrative section |
| `[Chorus]` | Hook/refrain |
| `[Bridge]` | Contrasting section |
| `[Intro]` | Opening |
| `[Outro]` | Closing |
| `[End]` | Hard stop |
| `[Instrumental]` | No vocals |
| `[Guitar Solo]` | Instrument feature |
| `[Fade Out]` | Gradual ending |
| `[Tag: descriptors]` | Per-section control |

### Creative Sliders cheat sheet

| Slider | Left | Center | Right |
| --- | --- | --- | --- |
| **Weirdness** | Conventional | Balanced | Experimental |
| **Style Influence** | Loose interpretation | Default | Strict adherence |
| **Audio Influence** | Minimal reference | Balanced | Strong reference |

### Pricing quick reference

| Free | Pro ($10/mo) | Premier ($30/mo) |
| --- | --- | --- |
| Credits | 50/day | 2,500/mo | 10,000/mo |
| V5.5 | No | Yes | Yes |
| Commercial | No | Yes | Yes |
| Studio | No | No | Yes |

---

## Changelog

| Date | Change | Source |
| --- | --- | --- |
| 2026-07-25 | **Docket correction: dispositive motions are due April 9, 2027, not January 8.** Judge Saylor granted a joint motion to amend the scheduling order in UMG Recordings v. Suno on June 30, 2026 (ECF No. 251); the guide’s earlier date rested on a March 2026 secondary report the order supersedes. Key legal developments bullet and [32](#fn:32) now cite the docket directly and carry the full amended schedule. Also recorded: Suno’s on-record framing of the breach (“a limited security incident,” “no sensitive personal information was compromised,” “primarily involved outdated source code”) sits against HIBP’s verified field list of names, addresses, phone numbers, purchase records, and partial card data; the labels’ pending motion to expand the case from 560 to 61,026 works remains undecided. Product surface unchanged since July 22. Watches open: GEMA ruling July 31, Duration-slider help docs still unpublished, no filing yet cites the leaked source code. | [32](#fn:32) |
| 2026-07-22 | **Source-code leak + 55.3M-account breach added to the legal landscape.** July 15 reporting on leaked 2023–24 source code documents per-source training scraping (YouTube Music ~113,879 hours, Pond5, IMSLP, Genius, Deezer, and more), substantiating the labels’ stream-ripping allegations; the same incident exposed 55,282,226 accounts (HIBP-verified July 20, breach dated November 2025, Shai-Hulud npm worm via a compromised employee credential) with no individual notifications planned. New bullet in Key legal developments + user-facing password guidance. Events pre-date this window but were missed by earlier scans — escalated on relevance. Watches unchanged: GEMA ruling July 31; help center still hasn’t published Duration-slider range/tier details. | [42](#fn:43) [43](#fn:44) |
| 2026-07-21 | **Duration slider on web (July 20).** New Create-form control on web with V5.5: drag the Duration slider to pick song length before generating. Documented in the Quick Start and the Suno vs. traditional DAWs table. Suno’s help center has not yet published min/max range or tier scope; only release-notes facts are documented. No model, pricing, metatag, or API changes in the window. | [41](#fn:42) |
| 2026-07-17 | **Web Lyrics Editor redesign (July 9).** Suno rebuilt lyric writing on the web: **Lyricist** (a profile that saves and locks in your writing style), natural-language editing (“make this line funnier” applied in place), rhyme and alternate-phrasing suggestions on highlighted words/lines, song structure labels (Verse/Chorus/Outro — the UI surface for the same flow control as bracket meta tags), and a distraction-free full-screen editor with autosave. Documented in The Lyrics field and Tag behavior in V5.5. Changelog-only: iMessage keyboard extension shipped July 15 (iOS); custom soccer-anthem template added July 7 (mobile). No model/pricing/metatag-vocabulary/API change; V5.5 remains flagship, Pro $10/Premier $30 unchanged. | [40](#fn:41) |
| 2026-07-06 | **Canonical “Suno Tags and Meta Tags” section.** Retitled the Metatags Reference section to Suno Tags and Meta Tags and made it the canonical tag landing: meta tags vs style tags terminology, an all-category tags-at-a-glance table with copy-paste examples, a fully tagged starter lyric sheet, the `[no vocals]` answer (Instrumental toggle + `[Instrumental]` + Exclude field), and a Tag behavior in V5.5 subsection consolidating specifics already documented elsewhere in the guide. No new Suno facts; editorial consolidation only. ToC and internal anchors updated. | Editorial |
| 2026-07-01 | **GEMA ruling postponed + Spark incubator.** The Munich Regional Court moved its GEMA v. Suno decision from June 12 to **July 31, 2026** (“aus dienstlichen Gründen”) — still poised to be the first major European ruling on whether AI platforms must license training music (see Copyright and Legal Landscape). **Spark** (June 25): incubator for unsigned artists — grants, marketing funds, songwriting camps through at least March 2027; artists keep rights and choose distribution, but reporting flags a perpetual non-disparagement clause and a 60-day rival-tool exclusivity window (see Key legal developments). No model/metatag/pricing/API changes; V5.5 remains flagship. Title/description aligned to the evergreen CTR-audit form. | [38](#fn:39) [39](#fn:40) |
| 2026-06-16 | **Stem Separation overhauled into three named methods (June 11).** Suno replaced the old 2-stem/12-stem split with **Split from Mix** (pull any single instrument or voice into 2 stems — generalizes the old vocals/instrumental split), **Auto Split** (the classic up-to-12-category model), and **Advanced Split** (Premier-only: choose from nearly 100 instruments for a custom stem set); output is cleaner and artifact-free. Rewrote the Stem Separation and Export section and updated the plan-comparison table. No new model (V5.5 remains flagship), no pricing/credit/metatag/API change. | [37](#fn:38) |
| 2026-06-08 | Maintenance check (changelog-only; no body change). V5.5 (March 26, 2026) remains the flagship model — no V5.x point release, no V6, no metatag/Studio/Creative Slider/Voices/pricing/credit changes, no public API launch. Verified post-May-13 items, none of which alter the technical reference: Suno raised a $400M Series D at a $5.4B valuation (June 3) and teased a first “developed in partnership with the music industry” licensed model that begins rolling out “in the coming months” (announced but **not yet released**); mobile-app Create added vocal-gender selection, prompt memory, and a lyrics model selector (May 14); “Share from iOS Notes and Voice Memos” shipped (June 4); an official Voices best-practices post published (June 5). | [36](#fn:37) |
| 2026-05-13 | Currentness pass: updated pricing verification to May 2026, corrected credit accounting from “generations” to songs/two-song Create batches, tightened Voices limitations, refreshed GEMA decision date, softened API/indemnification claims to officially documented surfaces, fixed derivative FAQ structured-data drift, and restored the six-song Custom Models minimum from Suno’s v5.5 announcement. | Multiple |
| 2026-04-20 | Corrected Studio 1.2 scope to official additions (Remove FX, Warp Markers with Quantize, Alternates, grid/metronome Time Signature support); removed incorrect claims about Personas-in-Studio, Sounds library, and in-browser EQ being Studio 1.2 features. Softened V5 sample-rate claim from 48kHz to studio-grade per current docs. Corrected duration claim (4→8 minutes). Reframed WMG-era download caps as announced-but-unshipped. | Multiple |
| 2026-04-04 | Renamed Persona Voices to Voices to match the V5.5 interface and moved community-sourced prompt-adherence wording out of the current recommendation. |
| 2026-04-01 | V5.5 detail pass: added Voices, Custom Models, My Taste, UMG litigation context, and WMG licensing notes. Later primary-source passes removed unsupported feature-minimum, API, download, and legal-defense specifics. | [31](#fn:31) [32](#fn:32) [33](#fn:33) [34](#fn:34) |
| 2026-03-30 | Added V5.5: Voice Cloning with verification (Pro/Premier), Custom Models (up to 3 per subscriber), My Taste adaptive preferences (all users). Updated model access tables and pricing. | [30](#fn:30) |
| 2026-03-24 | Added MILO-1080 step sequencer (March 2026 launch). Added GEMA vs Suno lawsuit (Germany, first European legal challenge). | [28](#fn:28) [29](#fn:29) |
| 2026-03-12 | Added WavTool acquisition (June 2025) context to Studio DAW section | [27](#fn:27) |
| 2026-03-07 | Added Studio 1.2 context, bonus daily credits for paid tiers, WMG partnership details (licensed models, Songkick), copyright ownership language update | Multiple |
| 2026-03-04 | Publication review: fixed citation attributions ([1](#fn:1) split across verified sources), added V4.5 8-minute generation, before/after prompt examples, complete song walkthrough, “why” explanations for metatags and Creative Sliders, Western training bias citation, stem separation technical distinction, 6 new references [18](#fn:18)-[23](#fn:23), internal cross-links, stat opening | Quality review |
| 2026-03-04 | Quality review: added Key Takeaways, How to Use This Guide, Prompt Enhancement Helper section, expanded Persona Voices, wired all citations, fixed Udio/UMG citation, added annual pricing and top-up credit details | Quality review |
| 2026-03-03 | Guide created covering V5, pricing, metatags, Studio, production workflows, licensing, and full prompt engineering reference | Multiple |
| 2026-02-01 | Suno Studio 1.2: warp markers, remove FX, alt takes, time signatures | [4](#fn:4) |
| 2025-09-25 | V5 (chirp-crow) released: studio-grade audio, Studio DAW, 12-stem separation, Persona Voices | [1](#fn:1) |
| 2025-11-01 | Warner Music settlement | [6](#fn:6) |
| 2025-05-01 | V4.5 released: 8-minute generation, Creative Sliders, Prompt Enhancement Helper | [19](#fn:19) |
| 2024-11-19 | V4 released: 4-minute generations, Covers, 2-stem separation | [3](#fn:3) |

---

## References

---

1. [Suno V5 Release and Review](https://bluelightningtv.com/2025/09/24/suno-v5-arrives-pro-grade-ai-music-goes-paid-only/). V5 (chirp-crow) released September 23–25, 2025. Studio-grade audio, higher mastered quality, Suno Studio DAW, 12-stem separation, Persona Voices. Third-party hubs sometimes report 48kHz and 44.1kHz for this model; Suno’s own marketing describes the improvement in production terms rather than naming a specific sample rate, so inspect an exported WAV if the exact rate matters for your pipeline. [↩](#fnref:1 "Jump back to footnote 1 in the text")[↩](#fnref2:1 "Jump back to footnote 1 in the text")[↩](#fnref3:1 "Jump back to footnote 1 in the text")[↩](#fnref4:1 "Jump back to footnote 1 in the text")[↩](#fnref5:1 "Jump back to footnote 1 in the text")[↩](#fnref6:1 "Jump back to footnote 1 in the text")[↩](#fnref7:1 "Jump back to footnote 1 in the text")
2. [Introducing Suno Studio](https://suno.com/blog/suno-studio). In-browser DAW for post-generation editing. Multi-track view, mix controls, stem isolation. [↩](#fnref:2 "Jump back to footnote 2 in the text")[↩](#fnref2:2 "Jump back to footnote 2 in the text")[↩](#fnref3:2 "Jump back to footnote 2 in the text")
3. [Suno Model Timeline](https://help.suno.com/en/articles/5782721). Official model version history from V2 through V5. [↩](#fnref:3 "Jump back to footnote 3 in the text")
4. [Suno Studio 1.2 Master Guide](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-studio-1-2-master-guide). February 2026 update: warp markers, remove FX, alternates, expanded time signature support. [↩](#fnref:4 "Jump back to footnote 4 in the text")[↩](#fnref2:4 "Jump back to footnote 4 in the text")
5. [Suno Rights & Ownership](https://help.suno.com/en/categories/550145). Commercial licensing: Pro and Premier users retain 100% of revenue. Free tier is non-commercial only. [↩](#fnref:5 "Jump back to footnote 5 in the text")[↩](#fnref2:5 "Jump back to footnote 5 in the text")[↩](#fnref3:5 "Jump back to footnote 5 in the text")
6. [WMG and Suno Partnership](https://suno.com/blog/wmg-partnership). Warner settled November 2025. Suno acquired Songkick, will develop WMG-licensed models. Artists retain control over name, image, likeness, voice usage. [↩](#fnref:6 "Jump back to footnote 6 in the text")[↩](#fnref2:6 "Jump back to footnote 6 in the text")[↩](#fnref3:6 "Jump back to footnote 6 in the text")
7. [UMG Settles Udio Lawsuit, Announces Partnership](https://musically.com/2025/10/30/umg-settles-udio-lawsuit-companies-plan-new-ai-music-service-together/). UMG and Udio settled October 29, 2025. New licensed AI music creation platform planned for 2026. Includes recorded music and publishing licenses. [↩](#fnref:7 "Jump back to footnote 7 in the text")
8. [US Copyright Office on AI-Generated Works](https://www.copyright.gov/ai/). Purely AI-generated works cannot be copyrighted. Works with sufficient human authorship may qualify. [↩](#fnref:8 "Jump back to footnote 8 in the text")
9. [gcui-art/suno-api](https://github.com/gcui-art/suno-api). Unofficial community wrapper for Suno. Not endorsed by Suno. May break without notice. [↩](#fnref:9 "Jump back to footnote 9 in the text")
10. [Suno Metatags Complete Guide](https://musci.io/blog/suno-tags). Community-compiled list of 500+ metatags for structure, vocals, instruments, and production. [↩](#fnref:10 "Jump back to footnote 10 in the text")
11. [Suno Creative Sliders Guide](https://help.suno.com/en/articles/6141377). Official documentation for Weirdness, Style Influence, and Audio Influence controls. [↩](#fnref:11 "Jump back to footnote 11 in the text")
12. [Suno Song Editor](https://help.suno.com/en/articles/6141505). Official documentation for Replace Section, Extend, Crop, and Fade operations. [↩](#fnref:12 "Jump back to footnote 12 in the text")
13. [Suno Pricing Plans](https://suno.com/pricing). Current tier comparison: Free, Pro, Premier; V5.5 access; credits; concurrent songs; add-on credits; top-up credit rules; and audio upload limits shown on the public pricing page. [↩](#fnref:13 "Jump back to footnote 13 in the text")[↩](#fnref2:13 "Jump back to footnote 13 in the text")[↩](#fnref3:13 "Jump back to footnote 13 in the text")[↩](#fnref4:13 "Jump back to footnote 13 in the text")[↩](#fnref5:13 "Jump back to footnote 13 in the text")[↩](#fnref6:13 "Jump back to footnote 13 in the text")
14. [Suno Prompt Engineering Best Practices](https://howtopromptsuno.com/making-music). Community guide for effective prompt structure and descriptor usage. [↩](#fnref:14 "Jump back to footnote 14 in the text")[↩](#fnref2:14 "Jump back to footnote 14 in the text")
15. [Suno AI Personas](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-ai-personas-update-dec-2025-what-changed-how-to-use-it). Persona creation, usage, and limitations. [↩](#fnref:15 "Jump back to footnote 15 in the text")[↩](#fnref2:15 "Jump back to footnote 15 in the text")[↩](#fnref3:15 "Jump back to footnote 15 in the text")
16. [Suno V5 Audio Specifications](https://musicmake.ai/fr/blog/suno-v5-audio-quality-khz-2026). Audio quality comparison across tiers: sample rate, bit depth, export formats. [↩](#fnref:16 "Jump back to footnote 16 in the text")
17. [The Suno API Reality](https://aimlapi.com/blog/the-suno-api-reality). Third-party analysis of official vs. unofficial API access. Used here only for unofficial wrapper risk; Suno’s own pricing and help center were checked in May 2026 and no official public developer API page was found. [↩](#fnref:17 "Jump back to footnote 17 in the text")
18. [Suno Hits 2M Paid Subscribers and $300M ARR](https://techcrunch.com/2026/02/27/ai-music-generator-suno-hits-2-million-paid-subscribers-and-300m-in-annual-recurring-revenue/). TechCrunch, February 2026. 7 million tracks generated per day; Spotify’s 100M-song catalog surpassed every two weeks. [↩](#fnref:18 "Jump back to footnote 18 in the text")[↩](#fnref2:18 "Jump back to footnote 18 in the text")
19. [Introducing V4.5](https://suno.com/blog/introducing-v4-5). Official Suno announcement. 8-minute single generation, Creative Sliders, Prompt Enhancement Helper, expanded genre accuracy, enhanced vocals. [↩](#fnref:19 "Jump back to footnote 19 in the text")[↩](#fnref2:19 "Jump back to footnote 19 in the text")[↩](#fnref3:19 "Jump back to footnote 19 in the text")
20. [Suno V5 (chirp-crow) Specifications](https://sunoaiwiki.com/news/2025/09-25-suno-v5-chirp-crow-api/). Third-party wiki page. Reports V5 internal model name chirp-crow, 320kbps export, Persona support, stem export. The same page reports a 48kHz sample rate; other third-party hubs report 44.1kHz for V5 and Suno’s own marketing does not name a specific rate. Treat the sample-rate figure as unverified until you inspect an exported WAV. [↩](#fnref:20 "Jump back to footnote 20 in the text")[↩](#fnref2:20 "Jump back to footnote 20 in the text")[↩](#fnref3:20 "Jump back to footnote 20 in the text")[↩](#fnref4:20 "Jump back to footnote 20 in the text")
21. [Missing Melodies: AI Music Generation and Its Omission of the Global South](https://arxiv.org/html/2412.04100v3). 86% of AI music training data comes from Global North genres. Guitar, piano, and drums comprise 52–67% of training clips; regional instruments under 3%. [↩](#fnref:21 "Jump back to footnote 21 in the text")
22. [Suno Stem Extraction](https://help.suno.com/en/articles/6141441). Official documentation for 2-stem (Vocals+Instrumental) and 12-track stem extraction. [↩](#fnref:22 "Jump back to footnote 22 in the text")[↩](#fnref2:22 "Jump back to footnote 22 in the text")
23. [Suno Separation Quality vs SpectraLayers](https://forums.steinberg.net/t/suno-separation-quality-vs-slp/995084). Discussion of how Suno’s stem export likely re-generates individual layers rather than performing post-hoc source separation. [↩](#fnref:23 "Jump back to footnote 23 in the text")[↩](#fnref2:23 "Jump back to footnote 23 in the text")[↩](#fnref3:23 "Jump back to footnote 23 in the text")
24. [Suno Pricing and Credit Details](https://suno.com/pricing). When monthly credits are exhausted, paid subscribers receive 50 bonus credits per day until the next billing cycle. [↩](#fnref:24 "Jump back to footnote 24 in the text")
25. [Suno Studio 1.2 announcement](https://suno.com/blog/studio1_2). Official Studio 1.2 additions: Remove FX, Warp Markers with Quantize, Alternates, and Time Signature support (grid/metronome, not model-conditioning). Personas and Suno Sounds are documented separately from Studio 1.2. [↩](#fnref:25 "Jump back to footnote 25 in the text")
26. Suno help center, [song ownership](https://help.suno.com/en/articles/2416769) and [copyright guidance](https://help.suno.com/en/articles/9602305). Paid subscribers own the songs made while subscribed for platform and commercial use; formal copyright protection depends on local law and is not guaranteed, especially for purely AI-generated works. [↩](#fnref:26 "Jump back to footnote 26 in the text")[↩](#fnref2:26 "Jump back to footnote 26 in the text")
27. [Suno Acquires WavTool](https://suno.com/blog/suno-acquires-wavtool). June 2025. Browser-based DAW with VST support, sample-accurate editing, AI features. Core team joined Suno in product and engineering leadership. [↩](#fnref:27 "Jump back to footnote 27 in the text")[↩](#fnref2:27 "Jump back to footnote 27 in the text")[↩](#fnref3:27 "Jump back to footnote 27 in the text")
28. [Suno’s Latest Move Is MILO-1080, An AI-Driven Step Sequencer](https://musically.com/2026/03/24/sunos-latest-move-is-milo-1080-an-ai-driven-step-sequencer). March 2026. 16-track step sequencer with text-to-sound generation, synth engine, MIDI support. Targets experienced producers. [↩](#fnref:28 "Jump back to footnote 28 in the text")[↩](#fnref2:28 "Jump back to footnote 28 in the text")
29. GEMA press release, [GEMA klagt gegen Suno](https://www.gema.de/de/w/gema-klagt-gegen-suno-2026), and Bavarian Ministry of Justice, [Verhandlung GEMA ./. Suno Inc.](https://www.justiz.bayern.de/gerichte-und-behoerden/landgericht/muenchen-1/presse/2026/6.php). March 9, 2026 hearing; decision announcement scheduled for June 12, 2026. [↩](#fnref:29 "Jump back to footnote 29 in the text")[↩](#fnref2:29 "Jump back to footnote 29 in the text")
30. [Introducing V5.5](https://suno.com/blog/v5-5). March 26, 2026. Voice Cloning with verification process (Pro/Premier), Custom Models personalized to user style (up to 3 per Pro/Premier subscriber), My Taste adaptive preference system (all users). [↩](#fnref:30 "Jump back to footnote 30 in the text")[↩](#fnref2:30 "Jump back to footnote 30 in the text")[↩](#fnref3:30 "Jump back to footnote 30 in the text")[↩](#fnref4:30 "Jump back to footnote 30 in the text")[↩](#fnref5:30 "Jump back to footnote 30 in the text")[↩](#fnref6:30 "Jump back to footnote 30 in the text")[↩](#fnref7:30 "Jump back to footnote 30 in the text")
31. Suno help center, [What’s New in v5.5](https://help.suno.com/en/articles/11362305), [Voices FAQ](https://help.suno.com/en/articles/11362433), [Voices: Use Your Voice in Suno](https://help.suno.com/en/articles/11362369), and [My Taste](https://help.suno.com/en/articles/11362561). Official guidance for Voices, Custom Models, My Taste, v5.5 model requirement, age/location restrictions, remix/cover behavior, Style Augmentation, and related v5.5 personalization behavior. [↩](#fnref:31 "Jump back to footnote 31 in the text")[↩](#fnref2:31 "Jump back to footnote 31 in the text")[↩](#fnref3:31 "Jump back to footnote 31 in the text")[↩](#fnref4:31 "Jump back to footnote 31 in the text")[↩](#fnref5:31 "Jump back to footnote 31 in the text")[↩](#fnref6:31 "Jump back to footnote 31 in the text")[↩](#fnref7:31 "Jump back to footnote 31 in the text")[↩](#fnref8:31 "Jump back to footnote 31 in the text")[↩](#fnref9:31 "Jump back to footnote 31 in the text")[↩](#fnref10:31 "Jump back to footnote 31 in the text")[↩](#fnref11:31 "Jump back to footnote 31 in the text")[↩](#fnref12:31 "Jump back to footnote 31 in the text")
32. [UMG Recordings, Inc. v. Suno, Inc., No. 1:24-cv-11611 (D. Mass.), docket](https://www.courtlistener.com/docket/68878608/umg-recordings-inc-v-suno-inc/). ECF No. 251, electronic order entered June 30, 2026, granting a joint motion to amend the scheduling order: “Dispositive Motions by 4/9/27.” Amended schedule: document production 7/30/26, fact discovery and depositions 9/30/26, requests for admission 10/14/26, expert disclosure 11/18/26, rebuttal 12/16/26, reply expert reports 1/15/27, expert depositions 3/5/27. Supersedes the earlier January 8, 2027 date reported by [chatgptiseatingtheworld.com](https://chatgptiseatingtheworld.com/2026/03/10/summary-judgment-in-umg-recordings-v-suno-pushed-back-to-jan-8-2027/) in March 2026. Verified against the docket July 25, 2026. [↩](#fnref:32 "Jump back to footnote 32 in the text")[↩](#fnref2:32 "Jump back to footnote 32 in the text")[↩](#fnref3:32 "Jump back to footnote 32 in the text")[↩](#fnref4:32 "Jump back to footnote 32 in the text")
33. [Universal Music Group Admits Foundational Legal Claim in Suno Case is Baseless](https://progresschamber.org/news/universal-music-group-admits-foundational-legal-claim-in-suno-case-is-baseless/). March 2026. UMG EVP Michael Nash stated “no indication that AI royalty dilution is a material issue for UMG from a revenue perspective.” [↩](#fnref:33 "Jump back to footnote 33 in the text")[↩](#fnref2:33 "Jump back to footnote 33 in the text")
34. [Suno Previews 2026 Changes Under Warner Music Deal](https://www.digitalmusicnews.com/2025/12/22/suno-warner-music-deal-changes/). Current models being phased out for WMG-licensed models. Download-cap specifics (free tier losing downloads, paid tier monthly caps) were described as forthcoming in the partnership announcement; as of May 2026 these caps have **not shipped** in Suno’s official help center. No retroactive licensing for songs created before subscribing. [↩](#fnref:34 "Jump back to footnote 34 in the text")[↩](#fnref2:34 "Jump back to footnote 34 in the text")[↩](#fnref3:34 "Jump back to footnote 34 in the text")
35. Suno help center, [How do I download my songs?](https://help.suno.com/en/articles/2409921) and [Why can’t I download WAV files?](https://help.suno.com/en/articles/2479873). Free users can download MP3/audio or video; Pro and Premier users can download WAV files in addition to MP3/M4A. [↩](#fnref:36 "Jump back to footnote 35 in the text")
36. June 8, 2026 maintenance check against primary Suno sources. [Series D announcement](https://suno.com/blog/series-d-announcement) (June 3, 2026): $400M raise at $5.4B post-money, plus a teased first licensed model “developed in partnership with the music industry” stated to roll out “in the coming months” (not yet released as of 2026-06-08). [Release notes](https://suno.com/release-notes): mobile Create gained vocal-gender selection, prompt memory, and a lyrics model selector (May 14); “Share from iOS Notes and Voice Memos” (June 4). [Suno blog](https://suno.com/blog): “Your Voice, Reimagined” Voices best-practices post (June 5). The flagship generation model remains V5.5 ([v5.5 blog](https://suno.com/blog/v5-5), March 26, 2026); the help-center model-timeline article is itself stale and still lists V5, so the v5.5 blog and release notes are the authoritative version sources. No metatag, Studio, Creative Slider, Voices/Persona, pricing/credit, or API changes in this window. [↩](#fnref:37 "Jump back to footnote 36 in the text")
37. [Suno release notes](https://suno.com/release-notes), “Stem Separation” update, June 11, 2026. Three methods: **Split from Mix** (“Pull any instrument or voice from the mix and get two stems: the instrument or voice, and everything else”); **Auto Split** (“Our classic model, splitting songs into 12 stem categories”); **Advanced Split** (“Choose exactly what to extract from a list of nearly 100 instruments” — “For Premier subscribers only”). The page markets the output as “cleaner, crisper, free from artifacts.” Only Advanced Split carries an explicit tier label (Premier); the page states no tier for Split from Mix or Auto Split, so this guide preserves the prior Auto Split (12-stem) Pro/Premier gating. Verified via primary source on 2026-06-16. [↩](#fnref:38 "Jump back to footnote 37 in the text")[↩](#fnref2:38 "Jump back to footnote 37 in the text")[↩](#fnref3:38 "Jump back to footnote 37 in the text")
38. GEMA v. Suno postponement: [CMS AI & Copyright case tracker — Germany, GEMA v. Suno](https://cms.law/en/int/publication/artificial-intelligence-and-copyright-case-tracker/germany-gema-v.-suno-judgment-scheduled-12-june-2026) and contemporaneous reporting ([aimusicpreneur](https://www.aimusicpreneur.com/ai-music-news/gema-suno-verdict-postponed-july-2026/)): the 42nd Civil Chamber of the Munich Regional Court moved the decision from June 12 to July 31, 2026, citing internal court reasons. Oral proceedings concluded March 2026. Current-session verification July 1, 2026 (PST). [↩](#fnref:39 "Jump back to footnote 38 in the text")[↩](#fnref2:39 "Jump back to footnote 38 in the text")
39. Suno Spark launch, June 25, 2026: [Variety](https://variety.com/2026/music/news/suno-spark-incubator-program-for-independent-artists-1236790684/), [Digital Music News](https://www.digitalmusicnews.com/2026/06/25/suno-spark-launch/), [The Hollywood Reporter](https://www.hollywoodreporter.com/music/music-industry-news/suno-reveals-incubator-program-for-indie-artists-1236630427/); participation-agreement fine print (perpetual non-disparagement, 60-day rival-tool exclusivity) per [Music Business Worldwide](https://www.musicbusinessworldwide.com/suno-is-paying-grants-to-independent-artists-so-long-as-they-agree-never-to-criticize-suno/). Program open to unsigned artists 18+, runs through at least March 2027; grants low-thousands to tens-of-thousands USD; artists retain rights and choose distribution. Current-session verification July 1, 2026 (PST). [↩](#fnref:40 "Jump back to footnote 39 in the text")[↩](#fnref2:40 "Jump back to footnote 39 in the text")
40. [Suno release notes](https://suno.com/release-notes), “Lyrics improvements on Web,” July 9, 2026. Redesigned web lyrics interface: **Lyricist**, a profile that saves and locks in your writing style; natural-language editing (type instructions like “make this line funnier” and the editor applies the change in place); rhyme and alternate-phrasing suggestions on highlighted words/lines; song structure labels (tag sections Verse/Chorus/Outro to tell the model how the track should flow); and a distraction-free full-screen editor with autosave. The same release-notes page lists the iMessage keyboard extension (July 15, 2026, iOS) and the custom soccer-anthem template (July 7, 2026, mobile). Verified via primary source on 2026-07-17. [↩](#fnref:41 "Jump back to footnote 40 in the text")[↩](#fnref2:41 "Jump back to footnote 40 in the text")[↩](#fnref3:41 "Jump back to footnote 40 in the text")
41. [Suno release notes](https://suno.com/release-notes), “Duration slider,” July 20, 2026: “Drag the new Duration slider in the Create form to pick your song length. Available on Web using V5.5 model.” Verified via primary source on 2026-07-21; help-center duration article not yet updated with range or tier details. [↩](#fnref:42 "Jump back to footnote 41 in the text")[↩](#fnref2:42 "Jump back to footnote 41 in the text")
42. [Hack Reveals Suno AI Music Generator Scraped YouTube, Deezer, and Genius](https://www.404media.co/hack-reveals-suno-ai-music-generator-scraped-youtube-deezer-and-genius/), 404 Media, July 15, 2026. Leaked 2023–24 source code lists per-source scraping volumes: YouTube Music 2,013,545 clips (113,879 hours), Pond5 62,117 hours, IMSLP 19,514 hours, Genius 17,615 hours, Deezer 12,287 hours, plus Jamendo, Freesound, MuseScore, and podcast RSS ingestion. [↩](#fnref:43 "Jump back to footnote 42 in the text")[↩](#fnref2:43 "Jump back to footnote 42 in the text")
43. [Have I Been Pwned: Suno breach entry](https://haveibeenpwned.com/api/v3/breach/Suno) (verified listing): 55,282,226 accounts; breach date November 25, 2025; added July 20, 2026; exposed emails, names, phone numbers, physical addresses, purchases, and partial card data. Attack vector per [CyberInsider](https://cyberinsider.com/data-breach-at-ai-music-service-suno-exposed-55-million-accounts/) (July 21, 2026): the Shai-Hulud npm worm via a compromised employee credential; Suno states the incident was detected and contained in November 2025 and that individual notifications were not required. [↩](#fnref:44 "Jump back to footnote 43 in the text")[↩](#fnref2:44 "Jump back to footnote 43 in the text")
