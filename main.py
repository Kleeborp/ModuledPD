#contacts.json
"""
Телефонный справочник (MVC)
"""

from Controller.phonebook_controller import PhoneBookController


def main():
    """Запуск приложения"""
    try:
        controller = PhoneBookController()
        controller.run()
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем")
    except Exception as e:
        print(f"Критическая ошибка: {e}")


if __name__ == "__main__":
    main()

