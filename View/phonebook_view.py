import os

CLEAR_CMD = "cls" if os.name == "nt" else "clear"

class PhoneBookView:
    @staticmethod
    def clear_screen():
        os.system(CLEAR_CMD)

    def show_menu(self, file_loaded = False):
        #PhoneBookView.clear_screen()
        if file_loaded:
            print("1. Открыть файл (v)")
        else:
            print("1. Открыть файл")
        print("""2. Сохранить файл
3. Показать все контакты
4. Создать контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход""")

    def get_menu_choice(self):
        """
            Получает выбор пункта меню от пользователя.

            Returns:
                int: Пункт меню 1-8

            Notes:
                Повторяет ввод при некорректных данных
            """

        while True:
            try:
                choice = input("Укажите пункт меню: ").strip()
                return int(choice)
            except ValueError:
                print("!Указан несуществующий пункт меню")

# view = PhoneBookView()
# view.show_menu()
# view.get_menu_choice()

    def show_all_contacts(self, contacts: list):
        "Показывает все контакты"

        #PhoneBookView.clear_screen()
        self.show_menu(file_loaded=True)

        if not contacts:
            print("!Сначала необходимо открыть файл")
        else:
            for contact in contacts:
                print(
                    contact["id"], ") ",
                    contact["name"], " - ",
                    contact["phone"], "; ",
                    contact["comment"]
                )
        input("\nДля возврата в меню, нажните Enter")

    def get_filename(self):
        "Получает название файла"

        while True:
            filename = input("Введите название файла:").strip()
            if filename == "contacts.json":
                return filename
            print("Неверное имя файла!")

    def get_search_query(self):
        """
            Получает поисковый запрос от пользователя.

            Returns:
                str: Текст для поиска
            """

        # PhoneBookView.clear_screen()
        self.show_menu(file_loaded=True)
        return input("Введите ФИО, номер телефона или ключевое слово:").strip()

    def show_search_result(self, contacts: list):
        "Показывает результаты поиска контактов"

        # PhoneBookView.clear_screen()
        self.show_menu(file_loaded=True)

        if not contacts:
            print("Ничего не найдено")
        else:
            for contact in contacts:
                print(
                    contact["id"], ") ",
                    contact["name"], " - ",
                    contact["phone"], "; ",
                    contact["comment"]
                )

        input("Для возврата в меню, нажмите Enter")

    def get_new_contact_data(self):
        """
            Собирает данные нового контакта с валидацией.

            Returns:
                tuple: (name: str, phone: int, comment: str)
            """
        # PhoneBookView.clear_screen()
        self.show_menu(file_loaded=True)

        name = input("Введите имя контакта: ").strip()

        while True:
            try:
                number = int(input("\nВведите номер контакта: ")).strip()
                break
            except ValueError:
                print("!Введён некорректный формат номера")

        comment = input("\nВведите комментарий: ").strip()

        return name, number, comment