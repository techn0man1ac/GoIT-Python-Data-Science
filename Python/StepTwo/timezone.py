from datetime import datetime, timezone, timedelta

utc_time = datetime.now(timezone.utc)
utc_timeUa = utc_time.astimezone(timezone(timedelta(hours=2))) 

local_now = datetime.now()
utc_now = datetime.now(timezone.utc)


print(local_now)    # 2024-04-21 15:45:56.036847
print(utc_now)      # 2024-04-21 12:45:56.036847+00:00
print(utc_timeUa)   # 2024-04-21 14:45:56.036847+02:00

# Припустимо, місцевий час належить до часової зони UTC+2
local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=2024, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Конвертація локального часу в UTC
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)  # Виведе час в UTC

#-------------------------

'''
Ці методи в datetime модулі роблять роботу 
з ISO форматом простою та ефективною, 
дозволяючи легко інтегрувати стандартизоване 
представлення дат та часу в Python-програми.
'''

# Час у конкретній часовій зоні
timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime(year=2024, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# Конвертація у формат ISO 8601
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone)

