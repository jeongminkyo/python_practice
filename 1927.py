import heapq

n = int(input())
pq = []
result = []

for _ in range(n):
    num = int(input())

    if num == 0:
        if len(pq) > 0:
            result.append((heapq.heappop(pq)))
        else:
            result.append(0)
    else:
        heapq.heappush(pq, num)

for i in result:
    print(i)