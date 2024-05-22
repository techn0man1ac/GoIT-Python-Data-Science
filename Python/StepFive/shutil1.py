import shutil

# Копіюємо файл
source_file = 'Python/StepFive/test.txt'
destination_dir = 'Python/StepFive/testShutil.txt'
shutil.copy(source_file, destination_dir)

# Копіюємо всю директорію
source_dir = 'Python/StepFive/testShutil'
destination_dir = 'Python/StepFive/testShutil_out'
shutil.copytree(source_dir, destination_dir)

'''
Окрім роботи з архівами модуль shutil може ще виконувати наступні високорівневі операції для обробки файлової системи:

shutil.copy(src, dst) копіює файл з src в dst. Якщо dst є директорією, файл буде скопійований зі своїм поточним іменем у цю директорію.
shutil.copytree(src, dst) рекурсивно копіює всю директорію src в директорію dst.
shutil.move(src, dst) переміщує файл або директорію src в dst.
shutil.rmtree(path) рекурсивно видаляє директорію path.
shutil.disk_usage(path) повертає статистику використання диска, що містить загальний об'єм, використаний об'єм і вільний об'єм 
для даного шляху.
'''