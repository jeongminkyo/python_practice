import sys

n = int(sys.stdin.readline())

num_list = [0 for _ in range(2000001)]

for _ in range(n):
    num = int(sys.stdin.readline())
    num += 1000000
    num_list[num] = 1

for i in range(2000001):
    if num_list[i] != 0:
        print((i - 1000000))