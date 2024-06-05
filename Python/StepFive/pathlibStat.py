from pathlib import Path
import time

file_path = Path("Python/StepFive/simple.jpg")

# Отримання розміру файлу
size = file_path.stat().st_size
print(f"Розмір файлу: {size} байтів") # Розмір файлу: 19674 байтів

# Час створення та модифікації
creation_time = file_path.stat().st_ctime 
modification_time = file_path.stat().st_mtime

print(f"Час створення: {time.ctime(creation_time)}") # Час створення: Wed May 22 13:01:15 2024
print(f"Час модифікації: {time.ctime(modification_time)}") # Час модифікації: Thu May 23 12:25:28 2024