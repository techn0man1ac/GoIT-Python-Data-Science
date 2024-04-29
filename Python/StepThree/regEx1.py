import re

file_name = "Мій документ Python.txt"
pattern = r"\s" # \s любий пробіл
replacement = "_"
formatted_name = re.sub(pattern, replacement, file_name)

print(formatted_name) # Мій_документ_Python.txt

text = "Python - потужна, універсальна;  мова!"
pattern = r"[;,\-:!\.]"
replacement = ""
modified_text = re.sub('  ', ' ', re.sub(pattern, replacement, text))
# Python  потужна універсальна мова -> Python потужна універсальна мова(замінив 2 пробіли "  " на один " ")
print(modified_text) 

phone = """
        Михайло Куліш: 050-171-1634
        Вікторія Кущ: 063-134-1729
        Оксана Гавриленко: 068-234-5612
        """
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2-\3"
formatted_phone = re.sub(pattern, replacement, phone)

print(formatted_phone)

'''
У цьому прикладі регулярний вираз (\d{3})-(\d{3})-(\d{4}) шукає 
телефонні номери в форматі XXX-XXX-XXXX. Кожна група чисел 
(\d{3} або \d{4}) поміщена в круглі дужки для збереження в групах. 
У рядку replacement, ми звертаємося до цих знайдених груп \1, \2, \3 
і вони відповідають першій, другій та третій групі відповідно. 
Ми кажемо, що першу групу наприклад треба помістити в круглі дужки. 
Далі пробіл та між групами залишити дефіс.
'''