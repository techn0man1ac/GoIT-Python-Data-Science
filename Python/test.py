from datetime import datetime
import pytz

# Встановлення місцевого часового поясу
local_tz = pytz.timezone('Europe/Kiev')

# Отримання поточного часу у місцевому часовому поясі
current_time = datetime.now(local_tz)

# Перевірка поточного часу
print(current_time)