N, L, K = map(int, input().split())

problem = []
for _ in range(N):
    sub1, sub2 = map(int, input().split())
    problem.append([sub1, sub2, False])

sort_problem = sorted(problem, key=lambda x:x[1])
cnt = 0
score = 0

for i in sort_problem:
    if L >= i[1] and cnt < K and not i[2]:
        cnt += 1
        score += 140
        i[2] = True

sort_problem = sorted(problem, key=lambda x:x[0])

for i in sort_problem:
    if L >= i[0] and cnt < K and not i[2]:
        cnt += 1
        score += 100
        i[2] = True

print(score)