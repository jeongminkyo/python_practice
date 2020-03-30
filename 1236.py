N, M = map(int, input().split(' '))

castle = []
count = 0
for _ in range(N):
    castle.append(input())

row = [0] * N
column = [0] * M

for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row[i] = 1
            column[j] = 1

row_count = 0
for i in range(N):
    if row[i] == 0:
        row_count += 1

column_count = 0
for i in range(M):
    if column[i] == 0:
        column_count += 1


print(max(row_count, column_count))