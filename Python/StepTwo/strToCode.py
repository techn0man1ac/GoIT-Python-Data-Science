def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes

result = string_to_codes("Hello world! Nice to meet you, Serhii")
print(result) #{'H': 72, 'e': 101, 'l': 108, 'o': 111, ' ': 32, 'w': 119, 'r': 114, 'd': 100, '!': 33, 'N': 78, 'i': 105, 'c': 99, 't': 116, 'm': 109, 'y': 121, 'u': 117, ',': 44, 'S': 83, 'h': 104}
print(sorted(result, key=len)) # ['H', 'e', 'l', 'o', ' ', 'w', 'r', 'd', '!', 'N', 'i', 'c', 't', 'm', 'y', 'u', ',', 'S', 'h']