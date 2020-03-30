import heapq

pq = []

n, m = map(int, input().split())
question = [0] * (n + 1)
solve_path = [[] for i in range(n+1)]
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    solve_path[a].append(b)
    question[b] += 1

for i in range(1, n+1):
    if question[i] == 0:
        heapq.heappush(pq, i)

while pq:
    result = heapq.heappop(pq)
    answer.append(result)

    for y in solve_path[result]:
        question[y] -= 1
        if question[y] == 0:
            heapq.heappush(pq, y)

for data in answer:
    print(data, end=' ')