import pytest
from Model.phonebook_model import PhoneBookModel


@pytest.fixture
def phonebook_model(tmp_path):
    """Создаём тестовый справочник"""
    model = PhoneBookModel()
    test_file = tmp_path / "contacts.json"
    model.file_name = str(test_file)
    model.contacts = [
        {"id": 1, "name": "Иван ИВАНОВ", "phone": 71234567890, "comment": "ДРУГ"},
        {"id": 2, "name": "Анна ПЕТРОВА", "phone": 79876543210, "comment": "коллега"},
        {"id": 3, "name": "Иван Сидоров", "phone": 71234567891, "comment": "отец"},
    ]
    model.data_len = 3
    return model
