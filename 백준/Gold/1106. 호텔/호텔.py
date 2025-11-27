import sys
input = sys.stdin.readline

C, N = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]

# dp[i] = i명까지 최소값
dp = [float('inf')] * (C + 101)
dp[0] = 0

for i in range(1, len(dp)):
    for cost, customer in cities:
        if i >= customer:
            dp[i] = min(dp[i], dp[i - customer] + cost)
        else:
            dp[i] = min(dp[i], cost)

print(min(dp[C:]))