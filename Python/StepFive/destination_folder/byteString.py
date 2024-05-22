byte_str = 'some text'.encode()
print(byte_str)

# Перетворення списку чисел у байт-рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # Виведе байтове представлення чисел b'\x00\x80\xff'

for num in [127, 255, 156]:
  print(hex(num))
  '''
    0x7f
    0xff
    0x9c
  '''