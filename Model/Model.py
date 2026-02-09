import json


class PhoneBookModel:
    def __init__(self):


    def open_file(self, filename):
        with open(filename, "r", encoding='utf-8') as f:
            data = json.load(f)
            return filename, data

    def save_file(self, filename, data):
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_contact(self, data, name_contact, number_contact, comment_contact):
        new_contact = {"id": int(len(data)) + 1, "name": name_contact, "phone": number_contact,
                       "comment": comment_contact}
        #data_len += 1

        with open(file_title, 'r', encoding='utf-8') as file:
            data = json.load(file)

        data.append(new_contact)

        #return data

    def find_contact(self, data, user_req):
        result = [contact for contact in data if user_req.lower() in str(data).lower()]
        return result

    def edit_contact(self, data):



