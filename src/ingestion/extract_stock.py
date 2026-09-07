import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests


def fetch_stock(ticker: str) -> dict[str, object]:
    response = requests.get(f'https://brapi.dev/api/v2/stocks/quote?symbols={ticker}', timeout=10)
    response.raise_for_status()

    data = response.json()

    return data


def build_file_path(ticker: str, collected_at: datetime) -> Path:
    year = collected_at.year
    month = collected_at.strftime("%m")
    day = collected_at.strftime("%d")

    name_archive = collected_at.strftime("%Y%m%dT%H%M%S%z") + ".json"
    file_path = (
        Path("data/raw/stocks")
        / ticker
        / str(year)
        / month
        / day
        / name_archive
    )
    return file_path


def save_json(data: dict[str, object], file_path: Path) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)


    with open(file_path, 'w', encoding='utf-8') as archive:
        json.dump(data, archive, indent=4, ensure_ascii=False)



def main () -> None:
    tickers = ["PETR4", "VALE3"]

    for ticker in tickers:

        try:
            data = fetch_stock(ticker)
            collected_at = datetime.now(ZoneInfo("America/Sao_Paulo"))
            file_path = build_file_path(ticker, collected_at)
            save_json(data,file_path)

            print (f"Arquivo em: {file_path}")

        except requests.exceptions.Timeout:
            print("A requisição expirou.")
        except requests.exceptions.RequestException as e:
            print(f"Ocorreu um erro: {e}")

    pass

if __name__ == "__main__":
    main()
