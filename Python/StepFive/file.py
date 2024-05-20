fh = open('Python/StepFive/test.txt', 'a') 
symbols_written = fh.write('hello!')
print(symbols_written) # 6
fh.close()
############
fh = open('Python/StepFive/test.txt', 'a+')
fh.write('hello!')
fh.seek(0) # Початок файлу

first_two_symbols = fh.read(8)
print(first_two_symbols)  # 'hello!he'
fh.close()
############
fh = open('Python/StepFive/test.txt', 'r')
all_file = fh.read()
print(all_file)  # 'hello!'

fh.close()
############
fh = open('Python/StepFive/test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol) # вивід по символу

fh.close()
############
fh = open('Python/StepFive/test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line) # вивід одним рядком

fh.close()
############
fh = open('Python/StepFive/test1.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('Python/StepFive/test1.txt', 'r')
#lines = fh.readlines() # ['first line\n', 'second line\n', 'third line']
lines = [el.strip() for el in fh.readlines()] # Забираємо \n
print(lines)

fh.close()