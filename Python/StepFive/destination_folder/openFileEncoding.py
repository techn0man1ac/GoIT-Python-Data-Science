# Відкриття текстового файлу з явним вказівкам UTF-8 кодування
with open('Python/StepFive/example4.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)