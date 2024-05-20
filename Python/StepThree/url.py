url_search_temp = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
url_search = url_search_temp.replace("<", "") # Забираю символ "<" напочатку з тимчасового рядка
url_search = url_search.replace(">", "")  # Забираю символ ">" вкінці та записую у url_search
print('url_search', url_search) 
# url_search https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t

_, query = url_search.split('?')
print(query) # q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query) 
# q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>
# {'q': 'Cat and dog', 'ie': 'utf-8', 'oe': 'utf-8', 'aq': 't'}

'''
Ми створюємо порожній словник obj_query
для зберігання параметрів запиту. 
Вираз query.split('&') розділяє рядок на 
окремі параметри за символом & та формує наступний список 
['q=Cat+and+dog', 'ie=utf-8', 'oe=utf-8', 'aq=t']. 
В середині циклу, кожен параметр el містить ключ та значення, 
розділені символом =. 
Спочатку ми розділяємо кожен параметр el на ключ та значення key, value = el.split('=').

Вираз obj_query.update({key: value.replace('+', ' ')}) 
додає пару ключ-значення до словника obj_query. 
Але ми ще виконуємо value.replace('+', ' ') 
і замінює символи + на пробіли, оскільки у 
URL пробіли зазвичай кодуються як +. 
Після завершення циклу виводиться оброблений 
словник obj_query, де ключі та значення відповідають параметрам запиту.
'''

import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
   print(html)