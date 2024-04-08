value_one = 11
value_two = 13
value_three = 3

if value_one != value_two and value_one != value_three and value_two != value_three:
    if value_one > value_two and value_one > value_three:
        print('Value one is the biggest')
    elif value_two > value_three:
        print('Value two is the biggest')
    else:
        print('Value three is the biggest')
elif value_one == value_two or value_one == value_three or value_two == value_three:
    if value_one > value_two and value_one == value_three:
        print('Value one and three are the biggest')
    elif value_two > value_three and value_two == value_one:
        print('Value two and one are the biggest')
    elif value_one < value_three == value_two:
        print('Value two and three are the biggest')
    else:
        print('All numbers equal')