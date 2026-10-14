#!/usr/bin/env python3
"""Генератор коротких ссылок rt1.ru/<код>/ → neurobober.com/digests/ с метками Matomo mtm_* (utm_* сайт срезает редиректом, 14.10).
Код = буква варианта (a/b/c = заход A/B/C) + номер 1..N. utm_content = код. Запуск: python3 gen-links.py"""
import json, os, html
TARGET = "https://neurobober.com/digests/"
VARIANTS = {"a": "A", "b": "B", "c": "C"}
N = 999
codes = {}
for letter, camp in VARIANTS.items():
    for i in range(1, N + 1):
        code = f"{letter}{i}"
        url = f"{TARGET}?mtm_source=tg_seller&mtm_medium=dm&mtm_campaign={camp}&mtm_content={code}&mtm_kwd={code}"
        codes[code] = url
        os.makedirs(code, exist_ok=True)
        u = html.escape(url, quote=True)
        open(f"{code}/index.html", "w", encoding="utf-8").write(f'''<!DOCTYPE html>
<html lang="ru"><head><meta charset="utf-8"><title>Нейробобер: дайджесты</title>
<meta name="robots" content="noindex,nofollow">
<meta http-equiv="refresh" content="0; url={u}">
<meta property="og:title" content="Дайджесты новостей — Нейробобер">
<meta property="og:description" content="Самое важное из сотен каналов и видео в одном месте. Ежедневные выжимки по ИИ, маркетингу, Авито, бизнесу и другим темам.">
<meta property="og:image" content="https://neurobober.com/og.png">
<script>location.replace({json.dumps(url)});</script></head>
<body><a href="{u}">Перейти на neurobober.com</a></body></html>
''')
json.dump({"target": TARGET, "codes": codes}, open("links.json", "w"), ensure_ascii=False, indent=1)
print(len(codes), "кодов")
