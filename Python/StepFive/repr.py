from datetime import datetime

test = datetime.now()

test_str = '12345'
test_list = [1, 2, 3]

print(str(test)) # 2024-05-13 20:15:18.596642
print(repr(test)) # datetime.datetime(2024, 5, 13, 20, 15, 18, 596642)

print(str(test_str)) # 12345
print(repr(test_str)) # '12345'

print(str(test_list)) # [1, 2, 3]
print(repr(test_list)) # [1, 2, 3]


print(test, test_str, test_list, sep='\n')