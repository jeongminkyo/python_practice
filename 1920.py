N = int(input())
A_list = list(map(int, input().split(' ')))

hash = {}
for num in A_list:
    hash[num] = True

M = int(input())
num_list = list(map(int, input().split(' ')))

for num in num_list:
    if num in hash:
        print(1)
    else:
        print(0)