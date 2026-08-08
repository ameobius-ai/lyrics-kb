# GigaChat second opinion

Advisory-прогон текстов через **GigaChat 3.5 Ultra** — «второе мнение» рядом с оценками Детектора 2.0.

## Роль в контуре

- Детектор 2.0, §4.5: граунд-трут — ухо и блайнд-чтение; внешняя оценка никогда не приёмочный гейт.
- Скрипт **не** определяет «человек/ИИ» (это чужая задача, см. §4.2 про GigaCheck) — он даёт редакторский вердикт: сильные/слабые строки, оценка 0–10, одна рекомендация.
- Сценарий канона: ручные прогоны на ключевых текстах (до/после REPAIR), не пакетные.

## Настройка (один раз)

1. В Sber Studio сгенерируй Authorization Key (scope `GIGACHAT_API_PERS`). Client ID/Secret нужны только Studio для генерации ключа — в код они не идут.
2. GitHub → репо → **Settings → Secrets and variables → Actions → New repository secret**:
   - Name: `GIGACHAT_AUTH_KEY`
   - Secret: Authorization Key целиком (base64-строка)
3. Опционально секрет/переменная `GIGACHAT_MODEL` — переопределить модель. По умолчанию `GigaChat-3.5-Ultra`; если API отклонит имя, скрипт сам возьмёт первую модель с «Ultra» из `/api/v1/models`.

## Lock зависимостей

`requirements.txt` содержит полный HTTP runtime graph из пяти exact pins: Requests, certifi, charset-normalizer, idna и urllib3. Workflow устанавливает только wheels в отдельный venv, выполняет `pip check`, а `check_dependency_lock.py` сверяет фактические версии с manifest и печатает fingerprint до появления GigaChat key в окружении.

Изменения lock проходят отдельный path-scoped clean-install check на Python 3.12. Вложенный manifest отслеживается собственным Dependabot pip-feed; обновление принимается только после зелёного install-smoke.

## Запуск

### Через GitHub Actions (рекомендуется)

Actions → **GigaChat second opinion** → Run workflow → укажи путь к файлу в репо (например `songwriting/ru/drafts/ottepel.md`). Workflow создаст отдельную ветку и PR с вердиктом рядом: `<name>.gigachat-opinion.md`; прямой push в исходную ветку не выполняется.

Путь должен быть относительным существующим `.md` внутри репозитория. Абсолютные пути, выход через `..`/symlink, `.git`, уже сгенерированные отчёты, управляющие символы и файлы больше 128 KiB отклоняются до внешнего API-вызова.

### Локально

Для SSL GigaChat нужны русские корневые сертификаты (Минцифры):

```bash
# Ubuntu/Debian — один раз:
sudo cp integrations/gigachat/certs/russian-trusted-root-ca.pem /usr/local/share/ca-certificates/russian-trusted-root-ca.crt
sudo cp integrations/gigachat/certs/russian-trusted-sub-ca.pem /usr/local/share/ca-certificates/russian-trusted-sub-ca.crt
sudo update-ca-certificates

# затем (из корня репозитория):
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --only-binary=:all: -r integrations/gigachat/requirements.txt
python -m pip check
python integrations/gigachat/check_dependency_lock.py
GIGACHAT_AUTH_KEY=... REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
  python integrations/gigachat/second_opinion.py songwriting/ru/drafts/ottepel.md
```

Файловый локальный режим применяет ту же repo-bound path policy. Режим `--stdin` остаётся доступен для явной локальной передачи текста.

## Контур безопасности workflow

- `lyrics_path` передаётся shell только через environment и quoted expansion.
- Checkout не сохраняет GitHub credential между steps.
- `GITHUB_TOKEN` появляется только в финальном publish-step и используется для новой ветки/PR.
- GigaChat key доступен только API-step; publish-step его не получает.
- HTTP runtime проверяется в изолированном venv до secret-bearing step.
- Path и dependency policies покрыты stdlib unit-тестами в blocking `validate`.

## Что на выходе

`*.gigachat-opinion.md` — модель, вердикт (3 сильные строки / 3 слабые с причиной / 0–10 / одна рекомендация), дисклеймер роли.
