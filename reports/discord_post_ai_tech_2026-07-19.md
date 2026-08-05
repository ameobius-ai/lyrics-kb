# Draft post — #аи-технологии

**Title line:**
Suno API + QC + genre packs — ship summary

**Body (RU, channel style):**

```
разложил что стырили с github (suno-cli + bitwize) и залил в kb

**suno api (reference)**
- studio-api endpoints, clerk→jwt, captcha preflight `/api/c/check`
- model keys: chirp-fenix = v5.5, crow/v5, bluejay/v4.5+
- persona create: 6 шагов upload→vox-stem→verify→create
- stems path: `/api/edit/stems/{id}` (не generate/stems)

**qc gates**
- lyrics: 13-point pre-gen checklist
- audio: 7-point post-master (lufs / tp / silence / phase / stereo / freq / crest)

**opendaw agent memory (theDAW ideas)**
- lineage + process history + smart export + prompt inference — в opendaw-mcp
- record_mix_pass / list_mix_history / export_for_platform / infer_suno_prompt

**genre packages (+6)**
darkwave · witch house · dark ambient · post-punk · hyperpop · drill
(было 3, стало 9). полный gap vs bitwize 387 — в reports/

kie.ai — не используем, только эндпоинты как справочник как ходит запрос к suno
```

Channel: Producers / #🔌〢аи-технологии  
Kanban: `t_69b2f209`
