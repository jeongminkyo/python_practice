from collections import deque

def is_cross_road(wei):
    queue = deque([begin])
    visited = [False] * (n + 1)
    visited[begin] = True
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= wei:
                visited[y] = True
                queue.append(y)
    return visited[des]


n, m = map(int, input().split(' '))
adj = [[] for _ in range(n+1)]
start = 1000000000
end = 1

for _ in range(m):
    start_node, end_node, weight = map(int, input().split(' '))
    adj[start_node].append((end_node, weight))
    adj[end_node].append((start_node, weight))
    start = min(start, weight)
    end = max(end, weight)

begin, des = map(int, input().split(' '))

result = start

while(start <= end):
    mid = (start + end) // 2

    if is_cross_road(mid):
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)