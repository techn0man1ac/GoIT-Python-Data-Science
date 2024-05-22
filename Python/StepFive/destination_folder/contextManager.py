with open("Python/StepFive/test3.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("Python/StepFive/test3.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)