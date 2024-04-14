pets = ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        # Випадок, коли є тільки собака
        print("There's a dog.")
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")

pets.insert(1, "cat") # ["dog", "fish", "cat"] -> ['dog', 'cat', 'fish', 'cat']
print(pets)
match pets:
    case ["dog", "cat", _, _]:
        print("There's a dog and a cat.") # Make job here case
    case ["dog", _, _, _]:
        print("There's a dog.")
    case _:
        print("No dogs.")