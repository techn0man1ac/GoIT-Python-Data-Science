fh = open('Python/StepFive/test2.txt', 'w+')
fh.write('hello!')

fh.seek(1)
second = fh.read(2)
print(second)  # 'el'

fh.close()
###############

fh = open("Python/StepFive/test2.txt", "w+")
fh.write("hello!")

position = fh.tell()
print(position)  # Позиція курсору 6

fh.seek(1)
position = fh.tell()
print(position)  # 1

fh.read(2)
position = fh.tell()
print(position)  # 3

fh.close()