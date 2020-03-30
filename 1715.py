import heapq

n = int(input())
pq = []
result = 0

for _ in range(n):
    num = int(input())
    heapq.heappush(pq, num)

while len(pq) != 1:
    one = heapq.heappop(pq)
    two = heapq.heappop(pq)
    sum_value = one + two
    result += sum_value
    heapq.heappush(pq, sum_value)

print(result)