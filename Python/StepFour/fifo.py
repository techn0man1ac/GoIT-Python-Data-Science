from collections import deque

# Створення черги
queue = deque()

# Enqueue: Додавання елементів
queue.append('a')
queue.append('b')
queue.append('c')

print("Черга після додавання елементів:", list(queue)) # ['a', 'b', 'c']

# Dequeue: Видалення елемента
print("Видалений елемент:", queue.popleft())

print("Черга після видалення елемента:", list(queue)) # ['b', 'c']

# Peek: Перегляд першого елемента
print("Перший елемент у черзі:", queue[0]) # ['b']

# IsEmpty: Перевірка на порожнечу
print("Чи черга порожня:", len(queue) == 0) # False

# Size: Розмір черги
print("Розмір черги:", len(queue)) # 2