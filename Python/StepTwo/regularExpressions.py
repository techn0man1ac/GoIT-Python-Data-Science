'''
Регулярні вирази:
. - один будь-який символ, крім рядка \n \
? - 0 або 1 входження шаблону зліва
'+' - 1 і більше входжень шаблону зліва
'*' - 0 і більше входжень шаблону зліва
\w - будь-яка цифра або буква [a-zA-Z0-9_] (\W - усе, крім букви або цифри [^a-zA-Z0-9_])
\d - будь-яка цифра [0-9] (\D - усе, крім цифри [^0-9])
\s - будь-який пробільний символ [\t\n\r\r\f\v] (\S - усе, окрім не пробільного символу [^ \t\n\r\r\f\v])
\b - межа слова
[...] - один із символів у дужках ([^...] - будь-який символ, крім тих, що в дужках)
\ - екранування спец.символів (приклад: . - означає крапку або + - знак "плюс")
^ і $ - початок і кінець рядка відповідно
{n,m} - від n до m входжень (приклад: {,m} - від 0 до m)
a|b - відповідає a або b
() - групує вираз і повертає знайдений текст
\t, \n, \r - символ табуляції, нового рядка та повернення каретки
'''


import re

string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
         "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
         "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
         "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
         "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

pattern = 'C:\\Test' # C:\Test Python з'їдає один слеш
print(pattern)
pattern = r'C:\\Test' # C:\\Test
print(pattern)

pattern = r'[0-9]+' #
result = re.search(pattern, string)
print(result) # <re.Match object; span=(39, 43), match='1858'>
print(result.span()) # (39, 43) - лиш індекс
first, last = result.span() 
print(string[first:last]) # 1858 - рік який я знайшов
print(result.group()) # 1858 - згрупувало, значно простіше а ніж з string[first:last]

result = re.findall(pattern, string)
print(result) # ['1858', '1911', '10', '1860', '1930', '1826', '1878', '1830', '1902', '11', '1881']

# result = re.findall(r'\s+', string)
# print(result)

pattern = r'\d+' # Еквівалентно r'[0-9]+' а плюс це зрупування символів, наприклад 11 або 1992
result = re.findall(pattern, string)
print(result)

pattern = r'[0-9]{4}' # 4 -тільки 4-х значні цифри
result = re.findall(pattern, string)
print(result) # ['1858', '1911', '1860', '1930', '1826', '1878', '1830', '1902', '1881']

pattern = r'[0-9]{2}' # Тільки двохзначні
result = re.findall(pattern, string)
print(result) # ['18', '58', '19', '11', '10', '18', '60', '19', '30', '18', '26', '18', '78', '18', '30', '19', '02', '11', '18', '81']

print('-' * 20)

pattern = r'\w+\.$'
result = re.findall(pattern, string)
print(result)

pattern = r'\w+\.'
result = re.findall(pattern, string)
print(result)

pattern = r'\w+'
result = re.findall(pattern, string)
print(result)

pattern = r'[a-zA-Z]+\.'
result = re.findall(pattern, string)
print(result)