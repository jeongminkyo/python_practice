import sys

N = int(sys.stdin.readline())

num_list = [0 for _ in range(10001)]
for _ in range(N):
    num = int(sys.stdin.readline())
    num_list[num] += 1

for idx, num in enumerate(num_list):
    if num > 0:
        for _ in range(num):
            print(idx)
