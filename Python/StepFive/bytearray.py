byte_array0 = bytearray(b'Kill Bill')
byte_array0[0] = ord('B')
byte_array0[5] = ord('K')
print(byte_array0)

byte_array1 = bytearray(b"Hello")
byte_array1.append(ord("!"))  
print(byte_array1)

byte_array1 = bytearray(b"Hello World")
string = byte_array1.decode("utf-8")
print(string)  # Виведе: 'Hello World'

'''
bytearray особливо корисний при обробці 
бінарних даних, наприклад, при читанні 
файлів у бінарному режимі, обробці мережевих 
пакетів, або при роботі з образами даних у пам'яті.
'''

byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))  
print(byte_array)

byte_array = bytearray(b"Hello World")
string = byte_array.decode("utf-8")
print(string)  # Виведе: 'Hello World'