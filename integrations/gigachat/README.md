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

## Запуск

### Через GitHub Actions (рекомендуется)

Actions → **GigaChat second opinion** → Run workflow → укажи путь к файлу в репо (например `songwriting/ru/drafts/ottepel.md`). Вердикт придёт коммитом рядом: `<name>.gigachat-opinion.md`.

### Локально

Для SSL GigaChat нужны русские корневые сертификаты (Минцифры):

```bash
# Ubuntu/Debian — один раз:
sudo cp integrations/gigachat/certs/russian-trusted-root-ca.pem /usr/local/share/ca-certificates/russian-trusted-root-ca.crt
sudo cp integrations/gigachat/certs/russian-trusted-sub-ca.pem /usr/local/share/ca-certificates/russian-trusted-sub-ca.crt
sudo update-ca-certificates

# затем:
python3 -m venv .venv && source .venv/bin/activate
pip install -r integrations/gigachat/requirements.txt
GIGACHAT_AUTH_KEY=... REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
  python integrations/gigachat/second_opinion.py songwriting/ru/drafts/ottepel.md
```

## Что на выходе

`*.gigachat-opinion.md` — модель, вердикт (3 сильные строки / 3 слабые с причиной / 0–10 / одна рекомендация), дисклеймер роли.
