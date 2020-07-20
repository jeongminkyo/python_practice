T = int(input())

for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))

    for i, val in enumerate(C):
        if val % 2 != 0:
            C[i] = val + 1

    cnt = 0
    while True:
        if len(set(C)) == 1:
            break

        result = []
        for i, val in enumerate(C):
            result.append((C[i % N - 1] // 2) - (val // 2))

        for i, val in enumerate(result):
            C[i] += val

        for i, val in enumerate(C):
            if val % 2 != 0:
                C[i] = val + 1

        cnt += 1

    print(cnt)
