from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from src.ingestion.extract_stock import build_file_path


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
