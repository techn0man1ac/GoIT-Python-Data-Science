import random

participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']

teams = []
for _ in range(5): # 5 команд по 2 людини
    team = random.sample(participants, 2)
    print(f"team: {team}") 
    for people in range(2): # 2 людини у команді
        participants.remove(team[people]) # Лише один елемент за раз
    teams.append(team) 

print(f"Команди: {teams}") 
# Команди: [['Йосип', 'Ігор'], ['Женя', 'Анна'], ['Зорян', 'Богдан'], ['Галина', 'Олена'], ['Дмитро', 'Віктор']]

'''
Всі унікальні, без повторень, до того робив ось так

team0 = random.sample(participants, 2)
participants.remove(team0[0])
participants.remove(team0[1])
team1 = random.sample(participants, 2)
participants.remove(team1[0])
participants.remove(team1[1])
team2 = random.sample(participants, 2)
participants.remove(team2[0])
participants.remove(team2[1])
team3 = random.sample(participants, 2)
participants.remove(team3[0])
participants.remove(team3[1])
team4 = random.sample(participants, 2)
participants.remove(team4[0])
participants.remove(team4[1])
'''

