input_str = input()

compare_str = input()
count = 0

while(True):
    if compare_str in input_str:
        count += 1
        start_index = input_str.find(compare_str)
        input_str = input_str[start_index + len(compare_str):]
    else:
        break

print(count)