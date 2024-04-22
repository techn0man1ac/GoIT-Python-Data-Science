from pathlib import Path

file_name = Path('./Python/StepFour/Temp')

try:
    with open(file_name / 'jokes.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

except Exception as e:
    print(f'{e} with file')