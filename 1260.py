import operator
import copy


class Node:
    def __init__(self, data):
        self.data = data
        self.vertax_list = []
        self.visit = False

    def dfs(self):
        if not self.visit:
            print(self.data, end=' ')
            self.visit = True

            if len(self.vertax_list) > 0:
                sorted_list = sorted(self.vertax_list, key=operator.attrgetter('data'))
                for node in sorted_list:
                    node.dfs()


def bfs(start_node_number, bfs_nodes):
    queue = [start_node_number]

    while len(queue) > 0:
        node_number = queue.pop(0)

        if node_number in bfs_nodes:
            if not bfs_nodes[node_number].visit:
                print(bfs_nodes[node_number].data, end=' ')
                bfs_nodes[node_number].visit = True

                if len(bfs_nodes[node_number].vertax_list) > 0:
                    sorted_list = sorted(bfs_nodes[node_number].vertax_list, key=operator.attrgetter('data'))
                    for node in sorted_list:
                        queue.append(node.data)


n, m, v = map(int, input().split())

nodes = {}

for _ in range(m):
    start, end = map(int, input().split())
    if start not in nodes:
        nodes[start] = Node(start)

    if end not in nodes:
        nodes[end] = Node(end)

    nodes[start].vertax_list.append(nodes[end])
    nodes[end].vertax_list.append(nodes[start])

bfs_nodes = copy.deepcopy(nodes)
nodes[v].dfs()
print()
bfs(v, bfs_nodes)
