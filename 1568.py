N = int(input())

count = 0
i = 1
while True:
    if i <= N:
        N -= i
        i += 1
        count += 1
    elif N > 0:
        i = 1
    else:
        break

print(count)