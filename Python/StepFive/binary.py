s = b'Hello!'
print(s[1])  # Виведе: 101 (це ASCII-код символу 'e')

cymbols = ''
for i in range(255):
    cymbols += chr(i)

print(cymbols)