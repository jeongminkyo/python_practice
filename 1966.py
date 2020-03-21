testcase = int(input())

for i in range(testcase):
    N, M = list(map(int, input().split(' ')))
    count = 1
    max_priority = 0
    queue = []
    input_value = list(map(int, input().split(' ')))

    for j in range(len(input_value)):
        queue.append([input_value[j], j])
        max_priority = max(max_priority, input_value[j])

    while len(queue) != 0:
        pop_value = queue[0]
        if pop_value[0] != max_priority:
            queue.append(pop_value)
            queue.pop(0)
        else:
            if pop_value[1] == M:
                print(count)
                break
            else:
                count += 1
                queue.pop(0)
                max_priority = 0
                for value in queue:
                    max_priority = max(max_priority, value[0])
