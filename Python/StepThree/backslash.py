print("Hello\nWorld")
'''
Hello
World
'''
print("Hello\tWorld") # Hello   World

'''
Виведення відбувається наступним чином: 
коли ми зустрічаємо символ \r, то повертаємося 
на початок рядка і продовжуємо виведення. 
Це перезаписує попередній вивід
'''
print("Hello my little\rsister") # sistermy little
'''
Керувальний символ \b забій (backspace).
Виведення здійснюється на один символ вліво
 та виконує вивід залишку після керувального символу
'''
print("Hello\bWorld") # HellWorld
'''
Також якщо нам треба виконати виведення зворотної косої риски.
'''
print("Hello\\World") # Hello\World
print('It\'s a beautiful day') # It's a beautiful day
print("He said, \"Hello\"") # He said, "Hello"