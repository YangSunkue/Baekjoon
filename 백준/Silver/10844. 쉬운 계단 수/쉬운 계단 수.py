# 다이나믹 프로그래밍
import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(12)] for _ in range(N + 1)]
for i in range(2, len(dp[1]) - 1):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(1, 11):

        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % int(1e9))