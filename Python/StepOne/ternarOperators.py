is_nice = False
state = "nice" if is_nice else "not nice"
print(state)

'''
Аналог

is_nice = True
if is_nice:
    state = "nice"
else:
    state = "not nice"

'''

some_data = None
msg = some_data or "No input datas"
print(msg)

'''
Аналог

some_data = None
if some_data:
    msg = some_data
else:
    msg =  "No input datas"

'''