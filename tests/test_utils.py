from src.utils import get_operations_data


def test_get_operations_data():
    test_path = r"C:\Users\User\PycharmProjects\BankFeature\data\test_file.json"
    assert get_operations_data(test_path) == [
        {"test_dict": "01", "test_key": "test_value_1"},
        {"test_dict": "02", "test_key": "test_value_2"},
    ]
