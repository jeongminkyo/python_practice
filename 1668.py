N = int(input())
num_list = []

for _ in range(N):
    num = int(input())
    num_list.append(num)

left_count = 1
visible_height = num_list[0]

for i in range(0, N-1):
    if num_list[i] < num_list[i+1] and num_list[i+1] > visible_height:
        left_count += 1
        visible_height = num_list[i+1]

print(left_count)

right_count = 1
visible_height = num_list[N-1]
for i in range(N-1, 0, -1):
    if num_list[i] < num_list[i-1] and num_list[i-1] > visible_height:
        right_count += 1
        visible_height = num_list[i - 1]

print(right_count)