N = int(input())
S = input()

bonus = 0
result = 0
for i, answer in enumerate(S, 1):
    if answer == 'O':
        result += i + bonus
        bonus += 1
    elif answer == 'X':
        bonus = 0

print(result)
