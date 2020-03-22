test_case = int(input())

for _ in range(test_case):
    stack = []
    password = input()
    append_data = []
    for i in password:
        if i == '<':
            if len(stack) != 0:
                append_data.append(stack.pop())
        elif i == '>':
            if len(append_data) != 0:
                stack.append(append_data.pop())
        elif i == '-':
            if len(stack) != 0:
                stack.pop()
        else:
            stack.append(i)

    stack.extend(reversed(append_data))

    print(''.join(stack))
