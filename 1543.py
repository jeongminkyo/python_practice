input_str = input()

compare_str = input()
index = 0
count = 0

while len(input_str) - index >= len(compare_str):
    if input_str[index:index + len(compare_str)] == compare_str:
        count += 1
        index += len(compare_str)
    else:
        index += 1

print(count)