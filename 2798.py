N, M = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))

sum = list()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum.append(cards[i]+cards[j]+cards[k])

sum.sort(reverse=True)

for i in sum:
    if i <= M:
        print(i)
        break