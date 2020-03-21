N, M = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_value = cards[i]+cards[j]+cards[k]
            if sum_value <= M:
                result = max(result, sum_value)

print(sum_value)