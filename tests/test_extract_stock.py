import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from unittest.mock import Mock

import pytest
import requests
from pytest import MonkeyPatch

from src.ingestion.extract_stock import build_file_path, save_json, fetch_stock


def test_build_file_path():
    collected_at = datetime(
        2026, 9, 7, 15, 30,
        tzinfo=ZoneInfo("America/Sao_Paulo"),
    )
    result = build_file_path("PETR4", collected_at)

    expected = Path(
        "data/raw/stocks/PETR4/2026/09/07/"
        "20260907T153000-0300.json"
    )

    assert result == expected

def test_save_json(tmp_path):
    data: dict[str, object] = {
        "ticker": "PETR4",
        "price": 35.50,
    }

    file_path = tmp_path / "raw" / "stocks" / "PETR4.json"

    save_json(data, file_path)

    assert file_path.exists()

    saved_data = json.loads(file_path.read_text(encoding="utf-8"))

    assert saved_data == data

def test_fetch_stock_success(monkeypatch: MonkeyPatch):
    expected_data: dict[str, object] = {
        "results": [
            {
                "symbol": "PETR4",
                "regularMarketPrice": 35.50,
            }
        ]
    }

    mock_response = Mock()
    mock_response.json.return_value = expected_data

    mock_get = Mock(return_value=mock_response)

    monkeypatch.setattr(
        "src.ingestion.extract_stock.requests.get",
        mock_get,
    )

    result = fetch_stock("PETR4")

    assert result == expected_data

    mock_get.assert_called_once_with(
        "https://brapi.dev/api/v2/stocks/quote?symbols=PETR4",
        timeout=10,
    )

    mock_response.raise_for_status.assert_called_once()
    mock_response.json.assert_called_once()


def test_fetch_stock_timeout(monkeypatch: MonkeyPatch):
    mock_get = Mock(side_effect=requests.exceptions.Timeout)

    monkeypatch.setattr(
        "src.ingestion.extract_stock.requests.get",
        mock_get,
    )

    with pytest.raises(requests.exceptions.Timeout):
        fetch_stock("PETR4")

    mock_get.assert_called_once_with(
        "https://brapi.dev/api/v2/stocks/quote?symbols=PETR4",
        timeout=10,
    )
