from pathlib import Path

old_dir = Path('./Python/StepFour/ABCtest.txt')
new_dir = Path('./Python/StepFour/ABCTemp/test_data.txt')

old_dir.rename(new_dir)