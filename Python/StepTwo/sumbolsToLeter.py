def reverse_string(num):
    chars = [chr(num + 96) for num in num_list]
    return ''.join(chars)

num = 5132
num_list = [int(digit) for digit in str(num)]
result = reverse_string(num_list)
print(result)