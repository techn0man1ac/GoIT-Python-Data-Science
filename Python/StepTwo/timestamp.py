from datetime import datetime

# Поточний час
now = datetime.now()

# Конвертація datetime в timestamp
timestamp = datetime.timestamp(now)
print(timestamp)  # Виведе timestamp поточного часу 1713696107.183136

# Припустимо, є timestamp
timestamp = 1713696107.183136

# Конвертація timestamp назад у datetime
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  # 2024-04-21 13:41:47.183136