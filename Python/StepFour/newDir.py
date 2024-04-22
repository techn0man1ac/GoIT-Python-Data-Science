from pathlib import Path

new_dir = Path('./Python/StepFour/ABC')

if not new_dir.exists():
    new_dir.mkdir()

new_dir.mkdir(exist_ok=True)