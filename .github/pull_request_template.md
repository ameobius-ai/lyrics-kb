## Чек-лист перед мерджем

<!-- Профилактика молчащих потерь при resolve конфликтов — см. issue #65 -->

- [ ] `python3 scripts/lint_patterns.py --self-test` прогнан локально на merge-base с актуальным main — все кейсы золотого корпуса зелёные
- [ ] Блокирующий sweep по живым текстам проходит: `find lyrics -name '*.md' ! -name 'README.md' -print0 | xargs -0 -r python3 scripts/lint_patterns.py` → exit 0
- [ ] Для НОВОГО флага детектора: пара кейсов (true positive + false-positive ловушка) добавлена в `references/golden_corpus.md` по протоколу §3, включая строку в сводной таблице ожиданий
- [ ] Проверка регистрации: флаг добавлен в `MECHANICAL_CHECKS`/`ADVISORY_CHECKS` И (для enforced) в `IMPLEMENTED_FLAG_NAMES` — self-test видит только канал `flags`
- [ ] `python3 validate.py` зелёный (index.json синхронизирован: count, файлы, дубли)
- [ ] `python3 scripts/check_encoding.py .` — ноль U+FFFD / не-UTF-8 байтов
- [ ] После мерджа: smoke-check на main — `grep -c "def check_<имя>" scripts/lint_patterns.py` ≥ 1 для каждого заявленного в PR флага
