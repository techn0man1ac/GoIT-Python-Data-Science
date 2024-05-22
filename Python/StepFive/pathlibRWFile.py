from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path("Python/StepFive/example_pathlib.txt")

# Запис тексту у файл
file_path.write_text("Привіт світ!", encoding="utf-8")

# Створення об'єкту Path для файлу
file_path = Path("Python/StepFive/pathlib/example.txt")

# Читання тексту з файлу
text = file_path.read_text(encoding="utf-8")
print(text)