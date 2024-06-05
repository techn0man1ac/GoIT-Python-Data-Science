def parse_input(user_input):
    # Функція розбиває введений рядок на команду та аргументи
    parts = user_input.strip().split(maxsplit=1)
    # Перша частина - команда (перетворюється до нижнього регістру)
    command = parts[0].lower()
    # Друга частина - аргументи, розділені пробілами
    args = parts[1].split() if len(parts) > 1 else []  # Перевірка наявності аргументів
    return command, args

def add_contact(args, contacts):
    # Додає новий контакт у словник контактів
    if len(args) != 2:
        return "Invalid command. Usage: add [username] [phone]"  # Повідомлення про неправильний формат команди
    username, phone = args
    contacts[username] = phone
    return "Contact added."

def change_contact(args, contacts):
    # Змінює номер телефону для існуючого контакту
    if len(args) != 2:
        return "Invalid command. Usage: change [username] [phone]"  # Повідомлення про неправильний формат команди
    username, phone = args
    if username not in contacts:
        return "Contact not found."  # Повідомлення, якщо контакт не знайдено
    contacts[username] = phone
    return "Contact updated."

def show_phone(args, contacts):
    # Виводить номер телефону для вказаного контакту
    if len(args) != 1:
        return "Invalid command. Usage: phone [username]"  # Повідомлення про неправильний формат команди
    username = args[0]
    if username not in contacts:
        return "Contact not found."  # Повідомлення, якщо контакт не знайдено
    return contacts[username]

def show_all(contacts):
    # Виводить усі контакти та їх номери телефонів
    if not contacts:
        return "No contacts found."  # Повідомлення, якщо список контактів порожній
    result = "\n".join([f"{username}: {phone}" for username, phone in contacts.items()])
    return result

def main():
    # Створення словника для збереження контактів
    contacts = {}
    print("Welcome to the assistant bot!")  # Повідомлення про початок роботи бота
    while True:
        user_input = input("Enter a command: ")  # Запит на введення команди від користувача
        command, args = parse_input(user_input)  # Розбиття введеної команди на команду та аргументи

        if command in ["close", "exit"]:
            # Завершення роботи бота, якщо отримана команда "close" або "exit"
            print("Good bye!")
            break
        elif command == "hello":
            # Вивід привітання, якщо отримана команда "hello"
            print("How can I help you?")
        elif command == "add":
            # Додавання нового контакту, якщо отримана команда "add"
            print(add_contact(args, contacts))
        elif command == "change":
            # Зміна номера телефону контакту, якщо отримана команда "change"
            print(change_contact(args, contacts))
        elif command == "phone":
            # Виведення номера телефону вказаного контакту, якщо отримана команда "phone"
            print(show_phone(args, contacts))
        elif command == "all":
            # Виведення усіх контактів та їх номерів телефонів, якщо отримана команда "all"
            print(show_all(contacts))
        else:
            # Повідомлення про невідому команду
            print("Invalid command.")

if __name__ == "__main__":
    main()
