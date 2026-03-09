import pytest


def test_add_contact(phonebook_model):
    """Тест добавления контакта.
    1) После добавления, длина списка контактов увеличивается на 1
    2) После добавления, ID нового контакта на 1 больше последнего в исходном справочнике"""

    initial_len = len(phonebook_model.contacts)
    last_id = list(phonebook_model.contacts[-1].values())[0]
    new_contact = phonebook_model.add_contact("Денис", 89136452386, "Друг")

    assert len(phonebook_model.contacts) == initial_len + 1
    assert new_contact == last_id + 1

@pytest.mark.parametrize(
    "query, expected_count, expected_ids",
    [   # query         кол-во        ID'шники
        ("иван",        2,            [1, 3]),      # по имени
        ("71234",       2,            [1, 3]),      # по номеру
        ("друг",        1,            [1]),         # по комментарию
        ("анна",        1,            [2]),         # точное имя
        ("",            0,            []),          # пустой запрос
        ("ИВАН",        2,            [1, 3]),      # регистр
    ]
)
def test_find_contact(phonebook_model, query, expected_count, expected_ids):
    """Параметризованный тест поиска"""
    results = phonebook_model.find_contact(query)

    assert len(results) == expected_count
    assert [contact["id"] for contact in results] == expected_ids


@pytest.mark.parametrize(
    "contact_id, new_name, new_phone, new_comment, expected_result",
    [
        # Изменение всех полей
        (1, "Иван Петров", 71234567891, "лучший друг", True),

        # Изменение только имени
        (2, "Анна Сидорова", None, None, True),

        # Изменение только номера
        (3, None, 71234567892, None, True),

        # Изменение комментария
        (1, None, None, "брат", True),

        # ID не найден
        (999, "Не существует", 1234567890, "test", False),
    ],
    ids=[
        "change_all_fields_id1",
        "change_name_only_id2",
        "change_phone_only_id3",
        "change_comment_only_id1",
        "id_not_found_999",
    ]
)
def test_edit_contact(phonebook_model, contact_id, new_name, new_phone, new_comment, expected_result):
    """Параметризованный тест изменения контакта"""

    initial_len = len(phonebook_model.contacts)
    result = phonebook_model.edit_contact(contact_id, name=new_name, number=new_phone, comment=new_comment)

    assert result == expected_result

    if expected_result:  # Контакт найден и изменён
        # Находим изменённый контакт
        contact = next(c for c in phonebook_model.contacts if c["id"] == contact_id)

        # Проверяем только изменённые поля
        if new_name is not None:
            assert contact["name"] == new_name
        if new_phone is not None:
            assert contact["phone"] == new_phone
        if new_comment is not None:
            assert contact["comment"] == new_comment

        # Проверяем НЕ изменённые поля
        if new_name is None:
            assert contact["name"] in ["Иван ИВАНОВ", "Анна ПЕТРОВА", "Иван Сидоров"]
        if new_phone is None:
            assert contact["phone"] in [71234567890, 79876543210, 71234567891]
        if new_comment is None:
            assert contact["comment"] in ["ДРУГ", "коллега", "отец"]

    else:  # ID не найден — состояние не изменилось
        assert len(phonebook_model.contacts) == initial_len
        assert phonebook_model._unsaved_changes is False    # Флаг не изменился

@pytest.mark.parametrize(
    "contact_id, expected_result, expected_final_len",
    [
        # Удаление существующего контакта
        (2, True, 2),    # Удаляем ID=2 → остаётся 2
        # ID не найден
        (999, False, 3), # ID не существует → остаётся 3
    ],
    ids=["delete_id_2", "id_not_found_999",]
)
def test_del_contact(phonebook_model, contact_id, expected_result, expected_final_len):
    """Параметризованный тест удаления контакта"""

    initial_len = len(phonebook_model.contacts)

    result = phonebook_model.del_contact(contact_id)

    assert result == expected_result

    if expected_result:  # Контакт удалён
        # Проверяем размер списка
        assert len(phonebook_model.contacts) == expected_final_len

        # Проверяем отсутствие контакта
        for contact in phonebook_model.contacts:
            assert contact["id"] != contact_id  # Отсутствует ID удалённого контакта

    else:  # ID не найден — состояние не изменилось
        assert len(phonebook_model.contacts) == initial_len



