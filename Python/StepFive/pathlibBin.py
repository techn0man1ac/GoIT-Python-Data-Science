from pathlib import Path

# Створення об'єкту Path для бінарного файлу
file_path = Path("Python/StepFive/example.bin")

# Бінарні дані для запису
data = b"Python is great!"

# Запис байтів у файл
file_path.write_bytes(data)

# Створення об'єкту Path для бінарного файлу
file_path = Path("Python/StepFive/example.bin")

# Читання байтів з файлу
binary_data = file_path.read_bytes()
print(binary_data)