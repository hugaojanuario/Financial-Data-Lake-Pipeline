from datetime import datetime

from zoneinfo import ZoneInfo

from pathlib import Path

import json

import requests

action = 'PETR4'

try:
    response = requests.get(f'https://brapi.dev/api/v2/stocks/quote?symbols={action}', timeout=10)
    response.raise_for_status()
    date = datetime.now(ZoneInfo("America/Sao_Paulo"))
    year = date.year
    month = date.strftime("%m")
    day = date.strftime("%d")

    data = response.json()

    print(data)
    print(response.status_code)

    name_archive = date.strftime("%Y%m%dT%H%M%SZ") + ".json"
    file_path = (
        Path("data/raw/stocks")
        / action
        / str(year)
        / month
        / day
        / name_archive
    )
    file_path.parent.mkdir(parents=True, exist_ok=True)


    with open(file_path, 'w', encoding='utf-8') as archive:
        json.dump(data, archive, indent=4, ensure_ascii=False)


except requests.exceptions.Timeout:
    print("A requisição expirou.")
except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro: {e}")
