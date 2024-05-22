import csv

character_banana = {'first_name': 'Baked', 'last_name': 'Banana'}
character_octopus = {'first_name': 'Lovely', 'last_name': 'Octopus'}
character_novelist = {'first_name': 'Sad', 'last_name': 'Novelist'}

with open('Python/StepSix/names.csv', 'w', newline='\n') as csvfile:
    field_names = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerow(character_banana)
    writer.writerow(character_octopus)
    writer.writerow(character_novelist)

with open('Python/StepSix/names.csv', 'r') as csvfile:
  print(csvfile.read())