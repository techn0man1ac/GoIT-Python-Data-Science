import shutil

# Створення ZIP-архіву example.zip з вмістом директорії 'StepFive'
shutil.make_archive('Python/StepFive/example', 'zip', root_dir='Python/StepFive/')

# Створення TAR.GZ архіву
shutil.make_archive('Python/StepFive/exampleGz', 'gztar', root_dir='Python/StepFive/')

# Розпакування ZIP-архіву в певну директорію
shutil.unpack_archive('Python/StepFive/example.zip', 'Python/StepFive/destination_folder')