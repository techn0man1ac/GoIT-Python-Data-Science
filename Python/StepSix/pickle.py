import pickle

data = {'some_key': 1234567890}

with open('Python/StepSix/my_dict.bin', 'wb') as file:
    pickle.dump(data, file)

data_types = pickle.dumps(data)
print(data_types)

with open("Python/StepSix/my_dict.bin", 'rb') as file:
    my_dict = pickle.load(file)

print(my_dict)
print(pickle.loads(data_types))