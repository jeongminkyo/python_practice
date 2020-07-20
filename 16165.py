N, M = map(int, input().split())

group_hash = {}
member_hash = {}
for _ in range(N):
    group_name, member_cnt = input(), int(input())

    for _ in range(member_cnt):
        member_name = input()
        member_hash[member_name] = group_name
        if group_name in group_hash:
            group_hash[group_name].append(member_name)
        else:
            group_hash[group_name] = [member_name]

for _ in range(M):
    name, type = input(), int(input())
    if type == 1:
        print(member_hash[name])
    else:
        res = sorted(group_hash[name])
        for i in res:
            print(i)
