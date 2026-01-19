"""
실버 3
DP
"""
import sys
input = sys.stdin.readline

N = int(input())
nums = [0, 0] + [int(input()) for _ in range(N)]

dp = [[0] * 2 for _ in range(N + 2)]

for i in range(2, N + 2):
    dp[i][0] = max(dp[i - 2]) + nums[i]
    dp[i][1] = dp[i - 1][0] + nums[i]

print(max(dp[-1]))