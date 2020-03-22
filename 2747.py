import sys

pivo = [0 for _ in range(46)]
pivo[1] = 1
for i in range(2, 46):
    pivo[i] = pivo[i-1] + pivo[i-2]

N = int(sys.stdin.readline())

print(pivo[N])
