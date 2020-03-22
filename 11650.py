N = int(input())

point_list = []
for _ in range(N):
    x, y = input().split()
    point_list.append((int(x), int(y)))

point_list = sorted(point_list, key=lambda element: (element[0], element[1]))

for point in point_list:
    print(point[0], point[1])