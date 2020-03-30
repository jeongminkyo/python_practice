class Node:
    def __init__(self, data, left, right, root):
        self.data = data
        self.left = left
        self.right = right
        self.root = root


def in_order(node, height):
    if node.left != -1:
        in_order(tree[node.left], height + 1)

    in_order_list.append((node.data, height))

    if node.right != -1:
        in_order(tree[node.right], height + 1)


N = int(input())
tree = {}
in_order_list = []

for i in range(1, N+1):
    tree[i] = Node(i, -1, -1, -1)

for _ in range(N):
    data, left, right = map(int, input().split(' '))
    tree[data].left = left
    tree[data].right = right

    if left != -1:
        tree[left].root = data
    if right != -1:
        tree[right].root = data

for i in range(1, N+1):
    if tree[i].root == -1:
        data = i

in_order(tree[data], 1)

temp_dic = {}

for index, i in enumerate(in_order_list):
    if i[1] in temp_dic:
        temp_list = temp_dic[i[1]]
        temp_list.append(index)
        temp_dic[i[1]] = temp_list
    else:
        temp_list = []
        temp_list.append(index)
        temp_dic[i[1]] = temp_list

print_level = 1
result = 0

for key in sorted(temp_dic.items()):
    if result < max(key[1]) - min(key[1]) + 1:
        result = max(key[1]) - min(key[1]) + 1
        print_level = key[0]

print(print_level, result)