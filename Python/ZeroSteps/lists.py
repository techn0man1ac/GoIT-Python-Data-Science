my_list = [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]
old_list = my_list.copy()
print(max(old_list), min(old_list))
my_list.append(16)
print(my_list)

# print(my_list[3])
my_list.insert(3, -100)
print(my_list)

my_list.pop()
print(my_list)

my_list.remove(-435)
print(my_list)

my_list.remove(235)
print(my_list)

my_list.pop(1)
print(my_list)

print(my_list.count(235))

print(len(my_list))