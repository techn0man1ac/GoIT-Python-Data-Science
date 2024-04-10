sentence_one = "Hello world"
sentence_two = "Hello " + "world"
# Відображення змінних
print(sentence_one, sentence_two, sep='\n')

# Перевірка рівності і ідентичності
print(f'Are sentence equal? {sentence_one == sentence_two}')
print(f'Are sentence identical? {sentence_one is sentence_two}')

# Перевірка місця збереження у пам'яті
print(f'Path of sentence in memory {id(sentence_one)}')
print(f'Path of sentence in memory {id(sentence_two)}')