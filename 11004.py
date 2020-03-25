n, k = map(int, input().split())

num_list = list(map(int, input().split()))

num_list = sorted(num_list)

print(num_list[k - 1])