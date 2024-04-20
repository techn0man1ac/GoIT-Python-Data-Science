morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

# Перетворення ключів словника на Unicode коди
table_morze_dict = {}
for k, v in morze_dict.items(): # Одночасно ітеруємо ключі і значення
    # print(k, v, sep='\t')
    table_morze_dict[ord(k)] = v

# for k in morze_dict: # Отримуємо ключі
#     print(k, morze_dict[k], sep='\t')

# for k in morze_dict.keys(): # Через ключі
#     print(k, morze_dict[k], sep='\t')
#
# for v in morze_dict.values(): # Лише по значеннях
#     print(v, sep='\t')
string = "Hello @world"

result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result) # ......-...-..--- @.-----.-..-..-..
result = ""

for ch in string:
    result = result + morze_dict.get(ch.upper(), ' ')

print(result) # ......-...-..---  .-----.-..-..-.. там де собачка - пробіл