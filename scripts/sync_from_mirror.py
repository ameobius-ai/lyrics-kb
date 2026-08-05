#!/usr/bin/env python3
"""Sync remote lyrics-kb content into local creative-studio/kb.

Snapshot utility (2026-08-04) for pulling mirror content from the live repo
Username-ame/lyrics-kb (private; token = Username-ame line in ~/.git-credentials,
gh CLI token is a DIFFERENT account — use git credentials, not gh).
- Clone fresh: git clone with token-in-URL remote into /tmp/lyrics-kb-full
  (or reuse existing full clone at REMOTE).
- Idempotent: skips files that already exist; only adds index.json entries
  for files not yet indexed (dedup by file/path, never by id).
- Cases get minimal frontmatter (id/track/status) so validate.py passes.
- Remote suno lane files land in suno/lanes/ (NOT packages/) — packages/ is
  validated for ## Style + ## Negatives headings.
Full pattern documented in skill: russian-lyrics-kb (Mirror repo → local KB sync).
"""
import json, os, re, shutil, subprocess, sys

LOCAL = "/home/ameobius/projects/creative-studio/kb"
REMOTE = "/tmp/lyrics-kb-full"
INDEX = os.path.join(LOCAL, "index.json")

# ---- 1. cases: copy with frontmatter, skip existing CW-001 ----
case_src = [
    "CW-002-trista-sorok-sem.md", "CW-003-razmorozka.md", "CW-004-chuzhoy-etazh.md",
    "CW-005-schetchik.md", "CW-006-vtoraya-smena.md", "CW-007-kruglosutochny.md",
    "CW-008-po-tu-storonu-kassy.md", "CW-009-dnevnoy-svet.md",
    "IND-001-third-pass.md", "IND-002-kill-the-crest.md",
    "MC-001-toxic.md", "SWP-010-mara.md", "SWP-011-shishiga.md",
    "SWP-012-staritsa.md", "SWP-013-bylichka.md",
]

def parse_status(text):
    m = re.search(r"Статус[^\n]*?[:*]*\s*([^\n·|]*)", text)
    if m:
        s = m.group(1).strip()
        if s:
            return s
    m2 = re.search(r"\*\*status[^\n]*", text)
    if m2:
        return m2.group(0).split(":")[-1].strip()
    return "pending_generation"

def parse_track(text):
    m = re.match(r"#\s+\S+\s*[—–-]\s*(.+)$", text)
    if m:
        return m.group(1).strip()
    return ""

copied_cases = []
for fn in case_src:
    src = os.path.join(REMOTE, "cases", fn)
    dst = os.path.join(LOCAL, "cases", fn)
    if os.path.exists(dst):
        continue
    with open(src, encoding="utf-8") as f:
        body = f.read()
    cid = fn.split("-")[0]
    track = parse_track(body)
    status = parse_status(body)
    fm = f"---\nid: {cid}\ntrack: {track}\nstatus: {status}\nsource: mirror lyrics-kb\n---\n\n"
    with open(dst, "w", encoding="utf-8") as f:
        f.write(fm + body)
    copied_cases.append(fn)

# ---- 2. plain copies ----
plain_dirs = [
    ("songwriting/anti-patterns.md", "songwriting/anti-patterns.md"),
    ("songwriting/cw-lessons.md", "songwriting/cw-lessons.md"),
    ("songwriting/industrial-danger-levers.md", "songwriting/industrial-danger-levers.md"),
    ("songwriting/swamp-playbook.md", "songwriting/swamp-playbook.md"),
    ("songwriting/top-texts-teardown.md", "songwriting/top-texts-teardown.md"),
    ("songwriting/en/EN_CRAFT_LAYER.md", "songwriting/en/EN_CRAFT_LAYER.md"),
    ("songwriting/ru/README.md", "songwriting/ru/README.md"),
    ("songwriting/ru/detector-2.0.md", "songwriting/ru/detector-2.0.md"),
    ("songwriting/ru/part-1-craft.md", "songwriting/ru/part-1-craft.md"),
    ("songwriting/ru/part-2-genres.md", "songwriting/ru/part-2-genres.md"),
    ("songwriting/ru/part-3-ops.md", "songwriting/ru/part-3-ops.md"),
    ("songwriting/ru/part-4-scoring.md", "songwriting/ru/part-4-scoring.md"),
    ("suno/coldwave.md", "suno/lanes/coldwave.md"),
    ("suno/industrial.md", "suno/lanes/industrial.md"),
    ("suno/metalcore.md", "suno/lanes/metalcore.md"),
    ("suno/swamp.md", "suno/lanes/swamp.md"),
    ("suno/style-tag-grammar.md", "suno/lanes/style-tag-grammar.md"),
    ("references/sound_corpus.md", "references/sound_corpus.md"),
    ("references/swamp-lane.md", "references/swamp-lane.md"),
    ("references/release-pipeline-v1.md", "references/release-pipeline-v1.md"),
]
copied_plain = []
for src_rel, dst_rel in plain_dirs:
    src = os.path.join(REMOTE, src_rel)
    dst = os.path.join(LOCAL, dst_rel)
    if os.path.exists(dst):
        continue
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    copied_plain.append(dst_rel)

# ---- 3. gigachat integration dir ----
giga_src = os.path.join(REMOTE, "integrations", "gigachat")
giga_dst = os.path.join(LOCAL, "integrations", "gigachat")
copied_giga = []
if os.path.isdir(giga_src) and not os.path.exists(giga_dst):
    shutil.copytree(giga_src, giga_dst)
    copied_giga = ["integrations/gigachat"]

print("cases copied:", len(copied_cases))
print("plain copied:", len(copied_plain))
print("gigachat:", copied_giga)

# ---- 4. index.json update ----
def entry(eid, cat, title, fp, tags, summary, source="mirror lyrics-kb"):
    return {"id": eid, "category": cat, "title": title, "file": fp,
            "tags": tags, "summary": summary, "source": source, "added": "2026-08-04"}

case_titles = {
    "CW-002-trista-sorok-sem.md": ("ГИЛЬОТИНА / ТРИСТА СОРОК СЕМЬ", "darksynth/coldwave 112bpm, детектор 2.0, score 8.4, якорь кнопка 347"),
    "CW-003-razmorozka.md": ("РАЗМОРОЗКА", "кейс лейна, статус генерация, разбор формы"),
    "CW-004-chuzhoy-etazh.md": ("ЧУЖОЙ ЭТАЖ", "кейс лейна darksynth/coldwave"),
    "CW-005-schetchik.md": ("СЧЁТЧИК", "кейс лейна"),
    "CW-006-vtoraya-smena.md": ("ВТОРАЯ СМЕНА", "кейс лейна"),
    "CW-007-kruglosutochny.md": ("КРУГЛОСУТОЧНЫЙ", "кейс лейна"),
    "CW-008-po-tu-storonu-kassy.md": ("ПО ТУ СТОРОНУ КАССЫ", "кейс лейна"),
    "CW-009-dnevnoy-svet.md": ("ДНЕВНОЙ СВЕТ", "кейс лейна"),
    "IND-001-third-pass.md": ("THIRD PASS", "industrial/neurofunk кейс"),
    "IND-002-kill-the-crest.md": ("KILL THE CREST", "industrial/neurofunk кейс"),
    "MC-001-toxic.md": ("TOXIC", "металкор/пост-хардкор кейс"),
    "SWP-010-mara.md": ("МАРА", "болотный фолк-электроник, цикл ГАТЬ, score 8.6"),
    "SWP-011-shishiga.md": ("ШИШИГА", "болотный лейн кейс"),
    "SWP-012-staritsa.md": ("СТАРИЦА", "болотный лейн кейс"),
    "SWP-013-bylichka.md": ("БЫЛИЧКА", "болотный лейн кейс"),
}

new_entries = []
# all case files present in local cases/ (skip ones already indexed later)
for fn in sorted(os.listdir(os.path.join(LOCAL, "cases"))):
    if not fn.endswith(".md"):
        continue
    cid = fn.split("-")[0]
    slug = fn.replace(".md", "")
    title, summ = case_titles.get(fn, (fn.replace(".md", ""), "кейс из зеркала lyrics-kb"))
    new_entries.append(entry(f"case-{slug}", "cases", title, f"cases/{fn}", ["case", "lane", cid.lower()], summ))

playbook_entries = [entry(*t) for t in [
    ("songwriting-anti-patterns", "songwriting", "Анти-паттерны сонграйтинга", "songwriting/anti-patterns.md", ["songwriting", "anti-patterns"], "Что НЕ делать в лирике — канон хаба"),
    ("songwriting-cw-lessons", "songwriting", "CW-уроки (coldwave lessons)", "songwriting/cw-lessons.md", ["songwriting", "coldwave", "lessons"], "Выводы из кейсов CW-серии"),
    ("songwriting-industrial-levers", "songwriting", "Industrial danger levers", "songwriting/industrial-danger-levers.md", ["songwriting", "industrial", "levers"], "Рычаги риска в industrial-лирике"),
    ("songwriting-swamp-playbook", "songwriting", "Болотный плейбук", "songwriting/swamp-playbook.md", ["songwriting", "swamp", "playbook"], "Канон болотного лейна"),
    ("songwriting-top-texts", "songwriting", "Разбор топовых текстов", "songwriting/top-texts-teardown.md", ["songwriting", "teardown", "analysis"], "Разборы сильных текстов"),
    ("songwriting-en-craft-layer", "songwriting", "EN CRAFT LAYER", "songwriting/en/EN_CRAFT_LAYER.md", ["songwriting", "en", "craft"], "Английский слой крафта"),
    ("songwriting-ru-part1", "songwriting", "Энциклопедия RU ч.1: крафт", "songwriting/ru/part-1-craft.md", ["songwriting", "ru", "encyclopedia", "craft"], "Энциклопедия сонграйтинга RU — крафт"),
    ("songwriting-ru-part2", "songwriting", "Энциклопедия RU ч.2: жанры", "songwriting/ru/part-2-genres.md", ["songwriting", "ru", "encyclopedia", "genres"], "Энциклопедия RU — жанры"),
    ("songwriting-ru-part3", "songwriting", "Энциклопедия RU ч.3: ops", "songwriting/ru/part-3-ops.md", ["songwriting", "ru", "encyclopedia", "ops"], "Энциклопедия RU — операционка"),
    ("songwriting-ru-part4", "songwriting", "Энциклопедия RU ч.4: scoring", "songwriting/ru/part-4-scoring.md", ["songwriting", "ru", "encyclopedia", "scoring"], "Энциклопедия RU — скоринг"),
    ("songwriting-ru-detector", "songwriting", "Детектор 2.0", "songwriting/ru/detector-2.0.md", ["songwriting", "detector", "scoring"], "Детектор лирики 2.0 + скоринг 2.0"),
]]
lane_entries = [entry(*t) for t in [
    ("suno-style-tag-grammar", "suno", "Грамматика Style-промптов и behavior-тегов (канон лейнов)", "suno/lanes/style-tag-grammar.md", ["suno", "style", "grammar", "behavior-tags", "lanes"], "9 слотов Style строго по порядку, канон всех лейнов (зеркало Notion)"),
    ("suno-lane-coldwave", "suno", "Suno-пакет: darksynth/coldwave (лейн)", "suno/lanes/coldwave.md", ["suno", "package", "lane", "coldwave", "darksynth"], "BPM 105-115, Am/Em, deep baritone, якорь-король"),
    ("suno-lane-industrial", "suno", "Suno-пакет: industrial (лейн)", "suno/lanes/industrial.md", ["suno", "package", "lane", "industrial"], "Лейн industrial/neurofunk"),
    ("suno-lane-metalcore", "suno", "Suno-пакет: metalcore (лейн)", "suno/lanes/metalcore.md", ["suno", "package", "lane", "metalcore"], "Лейн металкор/пост-хардкор"),
    ("suno-lane-swamp", "suno", "Suno-пакет: болотный фолк-электроник (лейн)", "suno/lanes/swamp.md", ["suno", "package", "lane", "swamp"], "Лейн болото"),
]]
ref_entries = [entry(*t) for t in [
    ("ref-sound-corpus", "references", "Sound corpus — звуковые метрики и таргеты", "references/sound_corpus.md", ["references", "metrics", "targets"], "Звуковые метрики и таргеты по всем кейсам"),
    ("ref-swamp-lane", "references", "Swamp lane — хаб болотной полосы", "references/swamp-lane.md", ["references", "swamp", "lane"], "Хаб болотного лейна"),
    ("ref-release-pipeline", "references", "Release pipeline v1 — канон пайплайна", "references/release-pipeline-v1.md", ["references", "release", "pipeline"], "Канон пайплайна релизов"),
]]
giga_entries = [entry(*t) for t in [
    ("int-gigachat", "references", "GigaChat second opinion интеграция", "integrations/gigachat/README.md", ["integration", "gigachat", "second-opinion"], "Скрипт second_opinion.py + GitHub Action + серты Минцифры"),
]]

new_entries += playbook_entries + lane_entries + ref_entries + giga_entries

with open(INDEX, encoding="utf-8") as f:
    idx = json.load(f)
existing_files = {(e.get("file") or e.get("path")) for e in idx["entries"]}
added = [e for e in new_entries if (e.get("file") or e.get("path")) not in existing_files]
idx["entries"].extend(added)
idx["count"] = len(idx["entries"])
with open(INDEX, "w", encoding="utf-8") as f:
    json.dump(idx, f, ensure_ascii=False, indent=2)
print("index entries added:", len(added), "| total:", idx["count"])

# ---- 5. validate ----
r = subprocess.run([sys.executable, "validate.py"], cwd=LOCAL, capture_output=True, text=True)
print(r.stdout[-800:])
if r.returncode != 0:
    print("VALIDATE FAIL")
    sys.exit(1)
print("VALIDATE OK")
