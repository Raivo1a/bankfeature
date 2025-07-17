from unittest.mock import patch

from src.external_api import exchange


@patch("requests.get")
def test_convert_amount(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 5},
        "info": {"timestamp": 1752397092, "rate": 100},
        "date": "2025-07-13",
        "result": 500,
    }
    assert exchange("USD", 5) == 500
