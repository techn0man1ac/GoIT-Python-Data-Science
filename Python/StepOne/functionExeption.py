def sum_af_all_numbers(*numbers): # *args -> (2,3,4,5,6,7,7)
    print(numbers)
    sum = 0
    for value in numbers:
        try:
            sum += float(value)
        except TypeError:
            continue
        except ValueError:
            continue
    return sum

print(sum_af_all_numbers(1,2,3,4,5,'1000',6,7,8,9,0, 7.7001, 'true', False, 90, -10000, sum([1,2,3,4,99])))