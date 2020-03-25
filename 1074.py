def visit(N, x, y):
    global result

    if N == 2:
        if x == r and y == c:
            print(result)
            return
        result += 1

        if x == r and y + 1 == c:
            print(result)
            return
        result += 1

        if x + 1 == r and y == c:
            print(result)
            return
        result += 1

        if x + 1 == r and y + 1 == c:
            print(result)
            return
        result += 1
        return

    visit(N / 2, x, y)
    visit(N / 2, x, y + N / 2)
    visit(N / 2, x + N / 2, y)
    visit(N / 2, x + N / 2, y + N / 2)


result = 0
N, r, c = map(int, input().split(' '))
visit(2 ** N, 0, 0)
