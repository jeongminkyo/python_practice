N = int(input())

point_list = []
for _ in range(N):
    x, y = map(int, input().split())
    point_list.append((x, y))

point_list = sorted(point_list)

for point in point_list:
    print(point[0], point[1])