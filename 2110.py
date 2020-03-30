n, c = map(int, input().split(' '))

num_list = []
for _ in range(n):
    num_list.append(int(input()))

num_list = sorted(num_list)

end = num_list[-1] - num_list[0]
start = num_list[1] - num_list[0]
result = 0

while(start <= end):
    mid = (start + end) // 2
    value = num_list[0]
    count = 1

    for i in range(1, len(num_list)):
        if num_list[i] >= value + mid:
            value = num_list[i]
            count += 1

    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)