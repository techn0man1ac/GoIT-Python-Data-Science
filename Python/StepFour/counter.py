from collections import Counter

def num_counter(filename, n):
    with open(filename, 'r') as file:
        data = file.read()
    data_updated = [int(i) for i in data.split(',')]
    counter = Counter(data_updated)
    #print(counter)
    order = counter.most_common(len(counter))
    return order[:n], order[-n:]

most, least = num_counter('Python/StepFour/numbers.txt', 5)
print(f"Most {most} \nLeast {least}")