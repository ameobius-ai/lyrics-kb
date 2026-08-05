# Hermes / cliproxy / MCP — idea steal (2026-07-26)

> Source radar: GitHub agent/infra wave. **Patterns only** — no vendor drop-in, no free-tier ToS greyzone, no identity creation via GitHub API.
> Stack anchor: Hermes multi-profile · cliproxy `:8317` · MCP allowlist · skills curator · mem0/tencentdb · kanban · sovereignty (ToS, no secrets in chat).

## What we steal vs what we skip

| Source | Steal | Skip |
|---|---|---|
| **mcptrustchecker** (MIT, ★~169) | capability-flow trust model, pipeline stages, grade axes | full npm dep as runtime (optional later) |
| **engramory** (MIT, ★~97) | always-on memory discipline, typed notes, index, PORTING map for Hermes | second memory DB / vector store |
| **SkillOpt** (MS, MIT) | train skills with epochs + validation gates (text-space) | weight training, MS research stack |
| **nexus-llm-router** | Observe→Decide→Act, circuit breaker, budget, guardrail≠provider fail | replace cliproxy wholesale |
| **OmniRoute / FreeLLMAPI** | health failover, per-key caps, catalog hygiene ideas | free-tier stacking (ToS risk) |
| **openserp** | self-host SERP for research/outreach | as default web_search without smoke |
| **agentglass** | multi-agent mission-control UX ideas | new dashboard product |
| **dario**, full agent OS (lobe/mastra/echo) | — | skip (ToS / replace Hermes) |
| **serena / cognee** | — | heavy coding-IDE / graph memory dupe |

---

## 1. MCP Trust — steal for `llm-redteam` + MCP allowlist

**Source:** `illiahaidar/mcptrustchecker` methodology v1.11  
**License idea OK:** MIT patterns; do **not** copy AGPL trees.

### Pipeline to re-implement (or wrap CLI later)

```
INPUT → acquire → unicode → injection → capability → implementation
     → toxic-flow → supply-chain → posture → integrity → score
```

### Hard ideas (map to our MCP policy)

1. **Two axes (load-bearing):**
   - **Capability** = blast radius (what tools *could* do) → separate level, does **not** auto-fail grade
   - **Trust threat** = malice/negligence signals → **only this lowers grade**
2. **Normalized `ServerSurface`** — one object whether MCP came from stdio, HTTP, static manifest, client config, or package. Our allowlist should normalize the same way before scan.
3. **Toxic-flow** = cross-tool chains (read secret → exfil via fetch) not single-tool heuristics.
4. **Unicode / smuggling decode** before injection detectors (homoglyphs, bidi, zero-width).
5. **Supply-chain:** score against **published source** (npm/PyPI tarball), not marketing metadata.
6. **Methodology version on every score** — grades only comparable within one version (like our spectral SLA version tags).
7. **Corpus loop:** FP/FN full-population audit when changing rules (same spirit as our validate.py + genre gap reports).

### Hermes wiring (idea, not shipped)

- Pre-connect gate for any new MCP: surface normalize → threat scan → allow/deny
- SARIF or JSON findings into `docs/` redteam landscape (defensive curator)
- CI optional: `mcptrustchecker scan` on declared MCP list — **only after explicit `шиф`**

### Do not steal

- Running untrusted MCP “to see what happens”
- Auto-approve by star count

---

## 2. Engramory — steal for memory discipline (not storage engine)

**Source:** `tinqiao-oss/engramory` PORTING.md + rules-snippet + SKILL.md  
**They already name Hermes:** always-loaded = `AGENTS.md` / `.hermes.md` — **not** `SOUL.md` (persona slot). Skills = full protocol.

### Steal checklist

1. **Discipline, not DB** — one-file-per-fact + pointer index; no second handoff store.
2. **Always-on pointer** in host rules so memory fires even when skill not “relevant”.
3. **One canonical `<MEMORY_ROOT>`** — Engramory authority; no parallel mem dumps.
4. **Recall protocol:** read index → open only hooks that resolve **inside** root; `..` / symlink / absolute escape = broken pointer report, never open.
5. **Write protocol:** durable only; no secret *values*; dedupe; update in place; types `user | feedback | project | reference`; `feedback`/`project` need **Why:** + **How to apply:**.
6. **Project note** = resumable state (goal, status, decisions, blockers, next step) — same index as durable facts.
7. **Verify before act** — recalled memory may be stale (flags, versions, paths).
8. **Git-ignore memory root** if inside repo (machine-local detail).

### Map onto our stack

| Their | Ours |
|---|---|
| MEMORY.md index | compact mem0 / tencentdb index + optional file index for producers |
| always-on snippet | producers/default `AGENTS.md` memory block (not SOUL) |
| SKILL.md full protocol | skill `engramory-discipline` or patch existing memory skill |
| types user/feedback/project/reference | align with tencentdb persona/episodic/instruction + project notes |
| no parallel store | ban ad-hoc `*_handoff.md` sprawl; one project note |

### Steal phrase for AGENTS (short)

- start task → read index / open only in-root pointers  
- durable learn → one atomic note + index line; delete wrong  
- project continuity in `project` type, not chat paste  
- never store credentials; store stable pointers only  

---

## 3. SkillOpt — steal for skills curator

**Source:** Microsoft SkillOpt (text-space optimizer for frozen agents)

### Steal

1. Treat skills like trainable artifacts: **epochs, batch, validation gates** — edit natural language, not weights.
2. Trajectory-driven edits: skill change only if offline/online trajectory metrics improve.
3. Validation gate = skill must pass fixed eval set before promote (our skill_manage promote path).
4. Version skills; compare A/B skill text on same tasks.

### Hermes map

- `skill_manage` + curator: require mini-eval (3 golden prompts) before pin
- producers music skills: golden suno/mix cases as validation batch
- no full SkillOpt runtime required — process only

---

## 4. Nexus / gateway — steal for cliproxy patches (not replace)

**Source:** `Francis1998/nexus-llm-router` ARCHITECTURE + SAFETY

### Lifecycle

```
RECEIVED → CLASSIFIED → ROUTED → DISPATCHED → RESPONDED
                ↘ FALLBACK ↗
```

### Steal into cliproxy / Hermes model router

1. **Observe:** complexity / domain / latency need / token budget (even crude rules).
2. **Decide:** pluggable strategies (rule, cost, latency, A/B) → `RoutingDecision` + **fallback chain**.
3. **Act:** adapters with `complete/stream/estimate_cost/health_check`.
4. **Response normalization:** join **all** text parts (OpenAI list content, Gemini parts, Anthropic blocks) — never first element only (we hit empty/truncated answers when leading part is `thinking`/`tool_use`).
5. **Circuit breaker per provider:** open after N consecutive **dispatch** failures; cool-down; recover probe.
6. **Budget guardrail** per key / profile.
7. **Critical:** guardrail rejects (budget, already-open circuit) **must not** count as provider failures — keeps circuit = health only.
8. **Rate limit** token-bucket per API key id.
9. Timeouts dual: asyncio + HTTP client.

### Explicitly do NOT steal from OmniRoute/FreeLLMAPI

- free-tier multi-provider stacking as product default (ToS absolutism)
- “1.5B free tokens” marketing as ops policy

### Optional later (after `шиф`)

- gap doc: cliproxy features vs nexus checklist (health, circuit, part-join, budget)
- unit tests for multi-part content join on gemini/anthropic paths

---

## 5. OpenSERP — steal for research/outreach

**Source:** `karust/openserp` (user already linked)

### Steal

- self-host browser-rendered SERP (Google/Bing/Yandex/DDG…) for agent research
- keep keys/local; no third-party SERP SaaS for sensitive queries

### Hermes map

- optional tool behind allowlist for default/freelance research
- never community-krab shell; owner/ops only
- smoke before any cron

---

## 6. Agentglass — UX steal only

- multi-profile “mission control”: status of producers/default/redops gateways, last error, active agents
- map to existing `gateway_state.json` / profile-health cron — improve **presentation**, don’t new platform

---

## Priority backlog (ideas → work items; ship only with `шиф` / `делай mcp`)

| # | Item | Effort | Value |
|---|---|---|---|
| 1 | Write MCP surface normalizer + threat checklist (from mcptrust stages) into redteam docs | S | high |
| 2 | Paste Engramory always-on snippet into profile AGENTS (memory block), align mem0 rules | S | high |
| 3 | Skill promote gate: 3 golden tests before pin | S | med |
| 4 | cliproxy: multi-part content join + circuit “guardrail ≠ fail” semantics | M | high |
| 5 | openserp smoke (owner) | M | med |
| 6 | optional mcptrustchecker CLI on MCP list in CI | M | med |

---

## Anti-patterns (do not “steal”)

- Replace Hermes with lobe/mastra/echo
- Free-tier gateway as primary (ToS)
- Claude sub re-proxy (dario)
- Second memory database beside mem0/tencentdb
- Auto-merge vendor MCP without trust scan
- Create GitHub identity artifacts via API

---

## Provenance

- Radar date: 2026-07-26
- Method: GitHub API + raw README/methodology (no install, no clone required for this note)
- Related music radar (separate): deshimmer, StemForge, openDAW upstream — not in this file’s ship list
