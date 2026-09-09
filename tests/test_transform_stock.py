from src.transformation.transform_stock import transform_stock
import pytest

def test_transform_stock():
    # resposta simulada da api para o test:

    raw_data = {
        "results": [
            {
                "symbol": "PETR4",
                "data": {
                    "shortName": "PETROBRAS PN",
                    "longName": "Petróleo Brasileiro S.A.",
                    "currency": "BRL",
                    "regularMarketPrice": 35.50,
                    "regularMarketOpen": 35.00,
                    "regularMarketDayHigh": 36.00,
                    "regularMarketDayLow": 34.80,
                    "regularMarketPreviousClose": 34.90,
                    "regularMarketChange": 0.60,
                    "regularMarketChangePercent": 1.72,
                    "regularMarketVolume": 1000000,
                    "marketCap": 450000000000,
                    "regularMarketTime": "2026-09-08T13:40:00.000Z",
                },
            }
        ],
        "requestedAt": "2026-09-08T13:42:28.819Z",
    }

    result = transform_stock(raw_data)

    assert result["ticker"] == "PETR4"
    assert result["short_name"] == "PETROBRAS PN"
    assert result["price"] == 35.5
    assert result["open_price"] == 35.0
    assert result["day_high"] == 36.0
    assert result["day_low"] == 34.8
    assert result["previous_close"] == 34.9
    assert result["volume"] == 1000000
    assert result["requested_at"] == "2026-09-08T13:42:28.819Z"
    assert result["long_name"] == "Petróleo Brasileiro S.A."
    assert result["currency"] == "BRL"
    assert result["change"] == 0.6
    assert result["change_percent"] == 1.72
    assert result["market_cap"] == 450000000000
    assert result["market_time"] == "2026-09-08T13:40:00.000Z"

def test_transform_stock_with_empty_results():
    raw_data = {
        "results": [],
        "requestedAt": "2026-09-09T12:00:00.000Z",
    }

    with pytest.raises(ValueError):
        # O código executado dentro deste bloco precisa gerar ValueError
        transform_stock(raw_data)