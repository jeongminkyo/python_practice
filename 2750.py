N = int(input())

num_list = []
for _ in range(N):
    num_list.append(int(input()))

for i in range(N):
    min_index = i
    for j in range(i+1, N):
        if num_list[min_index] > num_list[j]:
            min_index = j

    num_list[i], num_list[min_index] = num_list[min_index], num_list[i]

for num in num_list:
    print(num)