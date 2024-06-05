from collections import UserDict

# Клас для представлення поля запису
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для представлення імені контакту
class Name(Field):
    pass

# Клас для представлення номера телефону
class Phone(Field):
    def __init__(self, value):
        # Перевірка та валідація формату номера телефону
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)

# Клас для представлення контакту, який містить ім'я та список телефонів
class Record:
    def __init__(self, name):
        self.name = Name(name)  # Ім'я контакту
        self.phones = []  # Список телефонів

    # Додавання телефону до списку телефонів
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    # Видалення телефону зі списку телефонів
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    # Редагування номера телефону
    def edit_phone(self, old_phone, new_phone):
        # Змінні для перевірки чи знайдений старий номер та чи є новий номер дійсним
        old_phone_found = False
        new_phone_valid = False
        # Перебираємо всі телефони у записі
        for p in self.phones:
            # Якщо номер збігається зі старим номером
            if p.value == old_phone:
                # Встановлюємо, що старий номер знайдений
                old_phone_found = True
                # Якщо новий номер має 10 цифр і є дійсним
                if len(new_phone) == 10 and new_phone.isdigit():
                    # Встановлюємо, що новий номер є дійсним
                    new_phone_valid = True
                    # Міняємо значення телефону на новий
                    p.value = new_phone
        # Якщо старий номер не знайдений
        if not old_phone_found:
            # Викидаємо виняток з відповідним повідомленням
            raise ValueError("Old phone number not found")
        # Якщо новий номер недійсний
        if not new_phone_valid:
            # Викидаємо виняток з відповідним повідомленням
            raise ValueError("New phone number must contain 10 digits")


    # Пошук телефону в записі за його значенням
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

    # Перевизначений метод для зручного виведення контакту у зрозумілому форматі
    def __str__(self):
        return f"Contact name: {self.name}, phones: {', '.join(str(p) for p in self.phones)}"

# Клас для представлення адресної книги
class AddressBook(UserDict):
    # Додавання запису до адресної книги
    def add_record(self, record):
        self.data[record.name.value] = record

    # Пошук запису за ім'ям
    def find(self, name):
        return self.data.get(name)

    # Видалення запису за ім'ям
    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Приклад використання
if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

        # Пошук конкретного телефону у записі John
        found_phone = john.find_phone("5555555555")
        if found_phone:
            print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")