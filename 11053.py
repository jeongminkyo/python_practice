n = int(input())

dp = [1] * n
num_list = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i):
        if num_list[j] < num_list[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
