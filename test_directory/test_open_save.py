import pytest
import json
from pathlib import Path


@pytest.mark.parametrize(
    "filename, expected_exception",
    [("contacts.json", None), ("other.json", FileNotFoundError)],
    ids=["valid_filename", "invalid_filename"],
)
def test_open_file(phonebook_model, filename, expected_exception):
    """Параметризованный тест открытия файла
    1) Проверяем выброс исключения, при неверном имени файла
    2) Проверяем корректность имени, при верном имени (а что ещё проверять?=))
    """

    if expected_exception:
        with pytest.raises(
            expected_exception,
            match="Файл other.json не найден. Файл должен называться 'contacts.json'",
        ):
            phonebook_model.open_file(str(filename))
    else:
        phonebook_model.open_file(str(filename))
        assert phonebook_model.file_name == "contacts.json"


def test_save_file(phonebook_model):
    """Успешное сохранение в открытый файл"""

    result = phonebook_model.save_file()
    assert result is True

    # Проверяем, что файл создался и содержит данные
    file_path = Path(phonebook_model.file_name)
    assert file_path.exists()

    # Читаем сохранённый JSON
    with open(file_path, "r", encoding="utf-8") as f:
        saved_data = json.load(f)

    assert len(saved_data) == 3
    assert saved_data[0]["name"] == "Иван ИВАНОВ"
    assert saved_data[1]["phone"] == 79876543210


def test_save_file_no_file_open(phonebook_model):
    """Исключение при отсутствии открытого файла"""

    # Сбрасываем file_name
    phonebook_model.file_name = None

    with pytest.raises(ValueError, match="!Сначала необходимо открыть файл"):
        phonebook_model.save_file()
