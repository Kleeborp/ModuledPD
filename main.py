# from Controller.phonebook_controller import PhoneBookController
#
#
#
# if __name__ == "__main__":
#     PhoneBookController.run()



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
    finally:
        print("До свидания!")


if __name__ == "__main__":
    main()

