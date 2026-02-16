from View.phonebook_view import PhoneBookView
from Model.phonebook_model import PhoneBookModel


class PhoneBookController:
    def __init__(self):
        self.view = PhoneBookView()
        self.model = PhoneBookModel()

    def run(self):
        """Основной цикл справочника"""

        while True:
            self.view.show_menu()
            choice = self.view.get_menu_choice()

            if choice == 1:
                self.open_file_menu()
            elif choice == 2:
                self.save_file_menu()
            elif choice == 3:
                self.show_contacts_menu()
            elif choice == 4:
                self.add_contact_menu()
            elif choice == 5:
                self.find_contact_menu()
            elif choice == 6:
                self.edit_contact_menu()
            elif choice == 7:
                self.del_contact_menu()
            elif choice == 8:
                self.exit_menu()
            else:
                self.view.show_error("!Указан несуществующий пункт меню\n")

    def first_open(self):
        """Проверяет открыт ли файл"""

        if not self.model.contacts:
            self.view.show_error("!Сначала необходимо открыть файл")
            return True

    def open_file_menu(self):
        """Пункт меню 1 - Открыть файл"""

        try:
            filename = self.view.get_filename()
            self.model.open_file(filename)
            self.view.show_success(f"Файл успешно открыт, контактов в списке: {self.model.data_len}\n")
        except FileNotFoundError as e:
            self.view.show_error(str(e))
        except ValueError as e:
            self.view.show_error(str(e))

    def save_file_menu(self):
        """Пункт меню 2 - сохранить файл"""

        try:
            if self.model.save_file():
                self.view.show_success("!Файл сохранён\n")
        except ValueError as e:
            self.view.show_error(str(e))
        except IOError as e:
            self.view.show_error(str(e))

    def show_contacts_menu(self):
        """Пункт меню 3 - показать все контакты"""

        self.view.show_all_contacts(self.model.contacts)

    def add_contact_menu(self):
        """Пункт меню 4 - добавление нового контакта"""

        if self.first_open():
            return
        try:
            new_name, new_number, new_comment = self.view.get_new_contact_data()
            self.model.add_contact(new_name, new_number, new_comment)
            self.view.show_success("Контакт успешно добавлен\n")
        except ValueError as e:
            self.view.show_error(str(e))

    def find_contact_menu(self):
        """Пункт меню 5 - поиск контакта"""

        if self.first_open():
            return
        query = self.view.get_search_query()
        if query:
            result = self.model.find_contact(query)
            self.view.show_search_result(result)

    def edit_contact_menu(self):
        """Пункт меню 6 - изменение контакта"""

        if self.first_open():
            return
        try:
            contact_id = self.view.check_id(self.model.contacts)

            if self.model.edit_contact(contact_id, **self.view.get_contact_changes()):
                self.view.show_success("Контакт успешно изменён\n")
            else:
                self.view.show_error("Ошибка редактирования")
        except ValueError as e:
            self.view.show_error(str(e))

    def del_contact_menu(self):
        """Пункт меню 7 - удаление контакта"""

        if self.first_open():
            return
        contact_id = self.view.check_id(self.model.contacts)

        if self.model.del_contact(contact_id):
            self.view.show_success("Контакт удалён\n")
        else:
            self.view.show_error("Ошибка удаления")

    def exit_menu(self):
        """Пункт меню 8 - выход"""

        if self.model._unsaved_changes:
            if self.view.ask_save_on_exit():
                self.save_file_menu()
        self.view.show_success("Всего хорошего!")
        exit()