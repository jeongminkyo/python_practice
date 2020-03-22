N = int(input())
A_list = set(map(int, input().split(' ')))

M = int(input())
num_list = list(map(int, input().split(' ')))

for num in num_list:
    if num in hash:
        print(1)
    else:
        print(0)