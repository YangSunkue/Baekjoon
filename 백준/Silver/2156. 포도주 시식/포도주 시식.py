"""
실버 1
DP
"""
import sys
input = sys.stdin.readline

N = int(input())
wine = [0, 0] + [int(input()) for _ in range(N)]

dp = [[0] * 3 for _ in range(N + 2)]
for i in range(2, N + 2):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = dp[i - 1][0] + wine[i]
    dp[i][2] = dp[i - 1][1] + wine[i]

print(max(dp[-1]))