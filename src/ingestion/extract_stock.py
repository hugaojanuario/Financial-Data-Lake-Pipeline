import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

tickers = ["PETR4", "VALE3"]

for ticker in tickers:


    try:
        response = requests.get(f'https://brapi.dev/api/v2/stocks/quote?symbols={ticker}', timeout=10)
        response.raise_for_status()
        date = datetime.now(ZoneInfo("America/Sao_Paulo"))
        year = date.year
        month = date.strftime("%m")
        day = date.strftime("%d")

        data = response.json()

        print(data)
        print(response.status_code)

        name_archive = date.strftime("%Y%m%dT%H%M%S%z") + ".json"
        file_path = (
            Path("data/raw/stocks")
            / ticker
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
