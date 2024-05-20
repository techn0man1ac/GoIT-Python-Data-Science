fh = open('Python/StepFive/text.txt', 'w')
try:
    # Виконання операцій з файлом
    fh.write('Some data')
finally:
    # Закриття файлу в блоку finally гарантує, що файл закриється навіть у разі помилки
    fh.close()