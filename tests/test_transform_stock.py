from src.transformation.transform_stock import transform_stock

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
    assert result["price"] == 35.5
    assert result["currency"] == "BRL"
    assert result["requested_at"] == "2026-09-08T13:42:28.819Z"
    assert result["change_percent"] == 1.72