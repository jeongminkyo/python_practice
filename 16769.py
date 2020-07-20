buckets = []

for _ in range(3):
    C, M = map(int, input().split())
    buckets.append([C, M])

for i in range(100):
    idx = (i % 3)
    next_idx = (idx + 1) % 3
    current_c, current_m = buckets[idx]
    next_c, next_m = buckets[next_idx]

    if current_m + next_m > next_c:
        current_m = (current_m + next_m) - next_c
        next_m = next_c
    else:
        next_m = (current_m + next_m)
        current_m = 0

    buckets[idx] = [current_c, current_m]
    buckets[next_idx] = [next_c, next_m]

for i in buckets:
    print(i[1])