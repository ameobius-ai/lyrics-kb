#!/usr/bin/env python3
"""
GigaChat second opinion — advisory-вердикт «второго мнения» для текстов канона.

Роль в контуре (Детектор 2.0, §4.5): граунд-трут — ухо и блайнд-чтение,
внешняя оценка никогда не приёмочный гейт. Скрипт кладёт вердикт GigaChat
РЯДОМ с оценками Детектора, а не вместо них. Сценарий канона — ручные
прогоны на ключевых текстах, не пакетные пайплайны.

Модель по умолчанию: GigaChat 3.5 Ultra (флагман). Переопределяется
переменной окружения GIGACHAT_MODEL. Если API отклоняет указанное имя,
скрипт запрашивает /api/v1/models и берёт первую модель с «Ultra» в имени.

Auth: только Authorization Key из env GIGACHAT_AUTH_KEY.
Client ID / Client Secret в коде не нужны: они используются в Studio,
чтобы сгенерировать Authorization Key.

Usage:
  GIGACHAT_AUTH_KEY=... python second_opinion.py path/to/lyrics.md
  cat lyrics.md | GIGACHAT_AUTH_KEY=... python second_opinion.py --stdin
"""

import os
import sys
import uuid
from pathlib import Path

import requests

OAUTH_URL = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
API_BASE = "https://gigachat.devices.sberbank.ru/api/v1"
SCOPE = os.environ.get("GIGACHAT_SCOPE", "GIGACHAT_API_PERS")
DEFAULT_MODEL = "GigaChat-3.5-Ultra"

SYSTEM_PROMPT = (
    "Ты — слепой второй читатель текстов песен. Оцени текст как литературный "
    "редактор: конкретика vs штампы, сдвиги регистра, пропеваемость, цельность "
    "образа. Сформулируй: 1) три самые сильные строки, 2) три самые слабые "
    "строки с причиной, 3) вердикт 0–10, 4) одна строка-рекомендация по правке. "
    "Без оценки «человек/ИИ» — это не твоя задача. Отвечай по-русски, коротко."
)


def get_access_token(auth_key: str) -> str:
    resp = requests.post(
        OAUTH_URL,
        headers={
            "Authorization": f"Basic {auth_key}",
            "RqUID": str(uuid.uuid4()),
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={"scope": SCOPE},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def list_models(headers: dict) -> list:
    resp = requests.get(f"{API_BASE}/models", headers=headers, timeout=30)
    resp.raise_for_status()
    return [m.get("id", "") for m in resp.json().get("data", [])]


def chat(headers: dict, model: str, lyrics: str) -> str:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": lyrics},
        ],
        "temperature": 0.3,
        "max_tokens": 900,
    }
    resp = requests.post(
        f"{API_BASE}/chat/completions",
        headers={**headers, "Content-Type": "application/json"},
        json=payload,
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def main() -> None:
    auth_key = os.environ.get("GIGACHAT_AUTH_KEY")
    if not auth_key:
        sys.exit("GIGACHAT_AUTH_KEY не задан. Добавь Authorization Key из Sber Studio.")

    if len(sys.argv) > 1 and sys.argv[1] == "--stdin":
        lyrics = sys.stdin.read()
        out_path = Path("second-opinion.gigachat.md")
    elif len(sys.argv) > 1:
        src = Path(sys.argv[1])
        lyrics = src.read_text(encoding="utf-8")
        out_path = src.with_suffix("").with_name(src.stem + ".gigachat-opinion.md")
    else:
        sys.exit("Укажи путь к файлу с текстом или --stdin.")

    if not lyrics.strip():
        sys.exit("Пустой ввод — нечего оценивать.")

    token = get_access_token(auth_key)
    headers = {"Authorization": f"Bearer {token}"}

    model = os.environ.get("GIGACHAT_MODEL", DEFAULT_MODEL)
    try:
        verdict = chat(headers, model, lyrics)
    except requests.HTTPError:
        # Имя модели могло отличаться — берём первую доступную Ultra.
        models = list_models(headers)
        ultra = next((m for m in models if "Ultra" in m), models[0] if models else None)
        if not ultra:
            raise
        model = ultra
        verdict = chat(headers, model, lyrics)

    report = (
        f"# GigaChat second opinion (advisory, не гейт)\n\n"
        f"Модель: `{model}`\n\n"
        f"{verdict}\n\n"
        f"---\n"
        f"Роль: второе мнение рядом с оценками Детектора (§4.5). "
        f"Граунд-трут — ухо и блайнд-чтение.\n"
    )
    out_path.write_text(report, encoding="utf-8")
    print(f"OK → {out_path}")


if __name__ == "__main__":
    main()
