import json


class PhoneBookModel:
    def __init__(self):
        self.contacts = []
        self.data_len = 0
        self.file_name = None
        self._unsaved_changes = False


    def open_file(self, filename: str):
        """
            Загружает контакты из JSON файла.

            Returns:
                tuple: (filename, contacts_list, len_contacts)

            Raises:
                FileNotFoundError: Файл не найден
                ValueError: Неверный JSON формат
            """
        try:

            with open(filename, "r", encoding='utf-8') as f:
                data = json.load(f)

            if not isinstance(data, list):
                raise ValueError("Файл должен содержать список контактов")

            self.contacts = data
            self.data_len = len(data)
            self.file_name = filename

        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {filename} не найден. Файл должен называться 'contacts.json'")
        except json.JSONDecodeError as e:
            raise ValueError(f"Ошибка JSON: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"Непредвиденная ошибка: {str(e)}")



    def save_file(self):
        """
            Сохраняет текущие контакты в JSON файл.

            Raises:
                ValueError: Нет открытого файла
            """

        if not self.file_name:
            raise ValueError("!Сначала необходимо открыть файл")

        save_filename = self.file_name
        self._unsaved_changes = False

        with open(save_filename, "w", encoding='utf-8') as f:
            json.dump(self.contacts, f, ensure_ascii=False, indent=4)
        return True

    def add_contact(self, name: str, number: int, comment: str):
        """
            Добавляет новый контакт в список.

            Returns:
                int: ID добавленного контакта

            Raises:
                ValueError: Некорректный номер телефона
            """

        if not isinstance(number, int):
            raise ValueError("!Введён некорректный формат номера")


        new_contact = {
            "id": self.data_len + 1,
            "name": name,
            "phone": number,
            "comment": comment
        }


        # добавляем новый контакт в список
        self.contacts.append(new_contact)
        self.data_len += 1

        # флаг изменений
        self._unsaved_changes = True

        return new_contact["id"]

    def find_contact(self, query: str):
        """
            Ищет контакты по запросу в любом поле.

            Returns:
                list: Список найденных контактов (может быть пустым [])
            """

        if not query.strip():
            return []

        query_lower = query.lower()
        result = []

        for contact in self.contacts:
            conact_lower = str(contact).lower()
            if query_lower in conact_lower:
                result.append(contact)

        return result


    def edit_contact(self, contact_id: int, name: str = None, number: str = None, comment: str = None):
        """
            Изменяет контакт по ID. Параметры None = поле не меняется.

            Returns:
                bool: True если контакт изменен, False если ID не найден

            Raises:
                ValueError: Некорректный формат номера телефона
        """
        for contact in self.contacts:
            if contact["id"] == contact_id:
                if name is not None:
                    contact["name"] = name
                if number is not None:
                    contact["phone"] = number
                if comment is not None:
                    contact["comment"] = comment
                self._unsaved_changes = True  # флаг изменений
                return True

        return False

    def del_contact(self, contact_id: int):
        """
            Удаляет контакт по ID.


            Returns:
                bool: True если контакт удален, False если ID не найден

            Returns:
                bool: True если контакт удален, False если ID не найден
            """
        for contact in self.contacts:
            if contact["id"] == contact_id:
                self.contacts.remove(contact)
                self.data_len -= 1
                self._unsaved_changes = True # флаг изменений
                return True

        return False

