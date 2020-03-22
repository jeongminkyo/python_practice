N = input()

array = []

for i in N:
    array.append(int(i))

array.sort(reverse=True)

return_str = ''
for i in array:
    return_str += str(i)

print(return_str)