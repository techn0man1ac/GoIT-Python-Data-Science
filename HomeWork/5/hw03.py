def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "This contact does not exist."
        except IndexError:
            return "Invalid command format."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def phone_contact(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

@input_error
def all_contacts(args, contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts available."

def main():
    contacts = {}
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "add":
            args = input("Enter the argument for the command: ").split()
            print(add_contact(args, contacts))
        elif command == "change":
            args = input("Enter the argument for the command: ").split()
            print(change_contact(args, contacts))
        elif command == "phone":
            args = input("Enter the argument for the command: ").split()
            print(phone_contact(args, contacts))
        elif command == "all":
            args = None
            print(all_contacts(args, contacts))
        elif command == "close" or command == "exit":
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

'''
Enter a command: add
Enter the argument for the command: Serhii +38012345678 
Contact added.
Enter a command: add
Enter the argument for the command: Ardriy +38012345677
Contact added.
Enter a command: phone 
Enter the argument for the command: Serhii
+38012345678
Enter a command: all 
Serhii: +38012345678
Ardriy: +38012345677
Enter a command: close
Good bye!
'''
