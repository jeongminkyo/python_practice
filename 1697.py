from collections import deque


def bfs(v):
    time = 0
    queue = deque([(v, time)])

    while queue:
        v = queue.popleft()
        visited[v[0]] = True

        if v[0] == k:
            print(v[1])
            break

        time = v[1] + 1
        for next_pos in (v[0] - 1, v[0] + 1, v[0] * 2):
            if 0 <= next_pos < MAX and not visited[next_pos]:
                queue.append((next_pos, time))

MAX = 100002
n, k = map(int, input().split())
visited = [False] * MAX
bfs(n)
