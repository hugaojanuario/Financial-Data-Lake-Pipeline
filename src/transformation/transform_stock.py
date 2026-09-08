from typing import Any


def transform_stock(raw_data: dict[str, Any]) -> dict[str, Any]:
    result = raw_data["results"][0]
    stock = result["data"]

    transformed_data = {
        "ticker": result["symbol"],
        "short_name": stock["shortName"],
        "price": stock["regularMarketPrice"],
        "open_price": stock["regularMarketOpen"],
        "day_high": stock["regularMarketDayHigh"],
        "day_low": stock["regularMarketDayLow"],
        "previous_close": stock["regularMarketPreviousClose"],
        "volume": stock["regularMarketVolume"],
        "requested_at": raw_data["requestedAt"],
        "long_name": stock["longName"],
        "currency": stock["currency"],
        "change": stock["regularMarketChange"],
        "change_percent": stock["regularMarketChangePercent"],
        "market_cap": stock["marketCap"],
        "market_time": stock["regularMarketTime"],
    }

    return transformed_data