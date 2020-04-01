n = int(input())

set_list = []

set_list.append(set(['1']))
set_list.append(set(['00', '11']))

for i in range(2, n):
    input_set = set([])
    for num_set in set_list[i-1]:
        input_set.add(num_set + '1')
        input_set.add('1' + num_set)
    for num_set in set_list[i-2]:
        input_set.add('00' + num_set)
        input_set.add('11' + num_set)
        input_set.add(num_set + '00')
        input_set.add(num_set + '11')

    set_list.append(input_set)

print(len(set_list[n-1]) % 15746)