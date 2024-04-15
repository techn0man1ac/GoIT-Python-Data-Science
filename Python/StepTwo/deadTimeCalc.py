from datetime import datetime

deadLineDate = input('Enter dedline day in format 2024-01-01: ')
requested_day = datetime.strptime(deadLineDate, '%Y-%m-%d').date()
today_date = datetime.now().date()
calcDedline = requested_day - today_date
print(f'The deadline will come in {calcDedline.days} days')