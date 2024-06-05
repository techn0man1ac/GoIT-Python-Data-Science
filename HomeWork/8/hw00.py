'''
goit-pycore-hw-08
'''

import pickle
from datetime import datetime, timedelta
from collections import UserDict

# Декоратор для обробки помилок
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)
    return wrapper

# Базовий клас для поля даних
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для імені
class Name(Field):
    pass

# Клас для телефону з валідацією
class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)

# Клас для дня народження з валідацією формату
class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

# Клас для запису контакту
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def has_birthday(self):
        return self.birthday is not None

    def __str__(self):
        birthday_info = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" if self.has_birthday() else ""
        return f"Contact name: {self.name}, phones: {', '.join(str(p) for p in self.phones)}{birthday_info}"

# Клас для адресної книги
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.now().date()
        next_week = today + timedelta(days=7)
        for record in self.data.values():
            if record.has_birthday():
                birthday_date = record.birthday.value.replace(year=today.year)
                if today <= birthday_date <= next_week:
                    upcoming_birthdays.append(record)
                elif birthday_date < today:
                    birthday_date = birthday_date.replace(year=today.year + 1)
                    if today <= birthday_date <= next_week:
                        upcoming_birthdays.append(record)
        return upcoming_birthdays

# Функція для серіалізації даних
def save_data(book, filename="HomeWork/8/addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

# Функція для десеріалізації даних
def load_data(filename="HomeWork/8/addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

# Функція для виводу телефону контакту
@input_error
def phone_contact(args, book: AddressBook):
    if len(args) < 1:
        return "Please provide a name."
    name = args[0]
    record = book.find(name)
    if record:
        if record.phones:
            return f"{record.name}: {', '.join(str(phone) for phone in record.phones)}"
        else:
            return "No phone numbers found for this contact."
    else:
        return "Contact not found."

# Функція для додавання контакту
@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        return "Please provide a name and phone number."
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

# Функція для зміни телефону контакту
@input_error
def change_contact(args, book: AddressBook):
    if len(args) < 2:
        return "Please provide a name and new phone number."
    name, new_phone = args
    record = book.find(name)
    if record:
        record.phones.clear()
        record.add_phone(new_phone)
        return "Phone number changed successfully."
    else:
        return "Contact not found."

# Функція для виводу всіх контактів
@input_error
def all_contacts(book: AddressBook):
    if book.data:
        return '\n'.join(str(record) for record in book.data.values())
    else:
        return "Address book is empty."

# Функція для додавання дня народження
@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        return "Please provide a name and birthday in format DD.MM.YYYY."
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added successfully."
    else:
        return "Contact not found."

# Функція для виводу дня народження контакту
@input_error
def show_birthday(args, book: AddressBook):
    if not args:
        return "Please provide a contact name."
    name = args[0]
    record = book.find(name)
    if record and record.has_birthday():
        return f"{record.name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"
    else:
        return "Contact not found or no birthday set."

# Функція для виводу днів народження на наступному тижні
@input_error
def birthdays(args, book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return "Upcoming birthdays:\n" + '\n'.join(f"{record.name}: {record.birthday.value.strftime('%d.%m.%Y')}" for record in upcoming_birthdays)
    else:
        return "No upcoming birthdays."

# Функція для розбору введених користувачем даних
def parse_input(user_input):
    parts = user_input.split()
    command = parts[0]
    args = parts[1:]
    return command, args

# Головна функція програми
def main():
    # Завантаження даних з файлу при запуску
    book = load_data()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            # Збереження даних у файл перед виходом
            save_data(book)
            break

        elif command in ["help", "?"]:
            print("Available commands: [close, exit], [hello, help, ?], [add, change, phone, all], [add-birthday, show-birthday, birthdays]")
        
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(phone_contact(args, book))

        elif command == "all":
            print(all_contacts(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

'''
Welcome to the assistant bot!
Enter a command: all
Contact name: Serg, phones: 1234567890, birthday: 06.05.1991
Contact name: Serhii, phones: 0987654321, birthday: 06.06.1991
Enter a command: phone
Please provide a name.
Enter a command: Phone Serg
Invalid command.
Enter a command: phone Serg 
Serg: 1234567890
Enter a command: ?
Available commands: [close, exit], [hello, help, ?], [add, change, phone, all], [add-birthday, show-birthday, birthdays]
Enter a command: change Serg 1111111111
Phone number changed successfully.
Enter a command: all        
Contact name: Serg, phones: 1111111111, birthday: 06.05.1991
Contact name: Serhii, phones: 0987654321, birthday: 06.06.1991
Enter a command: exit
Good bye!
'''