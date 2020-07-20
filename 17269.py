N, M = map(int, input().split())
A, B = input().split()

mapped_eng = { 'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3,
               'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X':2, 'Y': 2, 'Z': 1 }

mixed_name = []
score_name = []
new_arr = []

for i in range(max([N, M])):
    if i < N:
        mixed_name.append(A[i])

    if i < M:
        mixed_name.append(B[i])

for i in mixed_name:
    score_name.append(mapped_eng[i])

while True:
    for i in range(0, len(score_name)-1):
        new_arr.append((score_name[i] + score_name[i+1]) % 10)

    if len(new_arr) == 2:
        break
    else:
        score_name = new_arr
        new_arr = []

print_sum = ''

for i in new_arr:
    print_sum += str(i)

print(str(int(print_sum)) + '%')
