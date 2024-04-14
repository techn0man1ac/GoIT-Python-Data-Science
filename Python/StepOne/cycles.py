alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=",")
print("\n")
some_iterable = ["I", "II", "III", "IV", "V", "VI"]

for i in some_iterable:
    print(i,end="\n")

odd_numbers = [1, 3, 5, 7, 9] 
numbers= []

for i in range(len(odd_numbers)):
    numbers.insert(i, odd_numbers[i] ** 2) # [1, 9, 25, 49, 81]
print(numbers) 
