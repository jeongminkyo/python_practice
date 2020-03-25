def cal(num, operation, result):
    global n
    global result_set
    if num == n+1:
        cal_result = result.replace(' ', '')
        if eval(cal_result) == 0:
            result_set.add(result)
        return

    if operation == '+':
        result = result + '+' + str(num)
    elif operation == '-':
        result = result + '-' + str(num)
    elif operation == ' ':
        result = result + ' ' + str(num)

    cal(num + 1, '+', result)
    cal(num + 1, '-', result)
    cal(num + 1, ' ', result)


test_case = int(input())
set_list = []
for _ in range(test_case):
    result_set = set([])
    n = int(input())
    cal(2, '+', '1')
    cal(2, '-', '1')
    cal(2, ' ', '1')
    set_list.append(result_set)

for result_set in set_list:
    for result in sorted(result_set):
        print(result)
    print()