x = input()

input_list = x.split(' ')
result = ''

for index in range(len(input_list) - 1):
    if input_list[index] < input_list[index+1] and result == 'descending':
        result = 'mixed'
        break
    elif input_list[index] > input_list[index+1] and result == 'ascending':
        result = 'mixed'
        break
    elif input_list[index] < input_list[index+1]:
        result = 'ascending'
    elif input_list[index] > input_list[index+1]:
        result = 'descending'

print(result)