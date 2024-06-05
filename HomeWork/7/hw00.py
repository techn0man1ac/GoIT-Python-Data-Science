'''
https://github.com/techn0man1ac/goit-core-hw-07
'''

from datetime import datetime, timedelta
from collections import UserDict

# Декоратор для обробки помилок вводу
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)
    return wrapper

# Клас базового поля
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас поля з ім'ям
class Name(Field):
    pass

# Клас поля з номером телефону
class Phone(Field):
    def __init__(self, value):
        # Перевірка довжини і формату номера телефону
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)

# Клас поля з днем народження
class Birthday(Field):
    def __init__(self, value):
        try:
            # Перетворення строки в об'єкт datetime
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

# Клас запису контакту
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []  # Список номерів телефонів
        self.birthday = None  # День народження

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def has_birthday(self):
        return self.birthday is not None

    def __str__(self):
        # Форматування виводу запису контакту з днем народження (якщо він вказаний)
        birthday_info = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" if self.has_birthday() else ""
        return f"Contact name: {self.name}, phones: {', '.join(str(p) for p in self.phones)}{birthday_info}"

# Клас адресної книги
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
                birthday_date = record.birthday.value.replace(year=today.year)  # Встановлення поточного року для порівняння
                if today <= birthday_date <= next_week:
                    upcoming_birthdays.append(record)
                elif birthday_date < today:  # Якщо день народження вже минув у поточному році
                    birthday_date = birthday_date.replace(year=today.year + 1)  # Перенесення на наступний рік
                    if today <= birthday_date <= next_week:
                        upcoming_birthdays.append(record)
        return upcoming_birthdays

# Функція для виводу контакту за ім'ям та номерами телефонів
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

# Функція для додавання нового контакту або зміни наявного
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

# Функція для зміни номера телефону контакту
@input_error
def change_contact(args, book: AddressBook):
    if len(args) < 2:
        return "Please provide a name and new phone number."
    name, new_phone = args
    record = book.find(name)
    if record:
        record.phones.clear()  # Видаляємо всі наявні номери
        record.add_phone(new_phone)  # Додаємо новий номер
        return "Phone number changed successfully."
    else:
        return "Contact not found."

# Функція для виводу всіх контактів у адресній книзі
@input_error
def all_contacts(book: AddressBook):
    if book.data:
        return '\n'.join(str(record) for record in book.data.values())
    else:
        return "Address book is empty."

# Функція для додавання дня народження контакту
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

# Функція для виводу днів народження контактів, які відбудуться протягом наступного тижня
@input_error
def birthdays(args, book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return "Upcoming birthdays:\n" + '\n'.join(f"{record.name}: {record.birthday.value.strftime('%d.%m.%Y')}" for record in upcoming_birthdays)
    else:
        return "No upcoming birthdays."

# Функція для розбору введеного користувачем рядка на команду та аргументи
def parse_input(user_input):
    parts = user_input.split()
    command = parts[0]
    args = parts[1:]
    return command, args

# Головна функція програми
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")  # Запит користувача на введення команди
        command, args = parse_input(user_input)  # Розбір введеної команди

        if command in ["close", "exit"]:  # Завершення програми
            print("Good bye!")
            break

        elif command in ["help", "?"]:  # Виведення списку доступних команд
            print("Available commands: [close, exit], [hello, help, ?], [add, change, phone, all], [add-birthday, show-birthday, birthdays]")
        
        elif command == "hello":  # Виведення привітання
            print("How can I help you?")

        elif command == "add":  # Додавання контакту
            print(add_contact(args, book))

        elif command == "change":  # Зміна контакту
            print(change_contact(args, book))

        elif command == "phone":  # Пошук контакту за ім'ям
            print(phone_contact(args, book))

        elif command == "all":  # Виведення всіх контактів
            print(all_contacts(book))

        elif command == "add-birthday":  # Додавання дня народження контакту
            print(add_birthday(args, book))

        elif command == "show-birthday":  # Виведення дня народження контакту
            print(show_birthday(args, book))

        elif command == "birthdays":  # Виведення днів народження, які відбудуться наступного тижня
            print(birthdays(args, book))

        else:
            print("Invalid command.")  # Повідомлення про недійсну команду

if __name__ == "__main__":
    main()

'''
Welcome to the assistant bot!
Enter a command: add-birthday Serg 01.06.1991
Contact not found.
Enter a command: add Serhii 1234567899
Contact added.
Enter a command: add Ser 0987654321    
Contact added.
Enter a command: all                   
Contact name: Serhii, phones: 1234567899
Contact name: Ser, phones: 0987654321
Enter a command: add-birthday Ser 01.06.1991    
Birthday added successfully.
Enter a command: add-birthday Serhii 01.05.1991 
Birthday added successfully.
Enter a command: birthdays                      
Upcoming birthdays:
Ser: 01.06.1991
Enter a command: ?
Available commands: [close, exit], [hello, help, ?], [add, change, phone, all], [add-birthday, show-birthday, birthdays]
Enter a command: add
Please provide a name and phone number.
Enter a command: add Hello 1234567890
Contact added.
Enter a command: change
Please provide a name and new phone number.
Enter a command: change Hello 0987654321
Phone number changed successfully.
Enter a command: phone
Please provide a name.
Enter a command: phone Hello
Hello: 0987654321
Enter a command: exit
Good bye!
'''
