from unittest.mock import patch

from src.reader import read_csv_file, read_xlsx_file


@patch("pandas.read_csv")
def test_read_csv_file(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [
        {"test_dict": "01", "test_key": "test_value_1"},
        {"test_dict": "02", "test_key": "test_value_2"},
    ]
    assert read_csv_file("test_file_path.csv") == [
        {"test_dict": "01", "test_key": "test_value_1"},
        {"test_dict": "02", "test_key": "test_value_2"},
    ]


@patch("pandas.read_excel")
def test_read_xlsx_file(mock_read_xlsx):
    mock_read_xlsx.return_value.to_dict.return_value = [
        {"test_dict": "01", "test_key": "test_value_1"},
        {"test_dict": "02", "test_key": "test_value_2"},
    ]
    assert read_xlsx_file("test_file_path.xlsx") == [
        {"test_dict": "01", "test_key": "test_value_1"},
        {"test_dict": "02", "test_key": "test_value_2"},
    ]
