N = int(input())

user_list = []
for _ in range(N):
    age, name = input().split()
    user_list.append((int(age), name))

user_list = sorted(user_list, key=lambda x: x[0])

for user in user_list:
    print(user[0], user[1])
