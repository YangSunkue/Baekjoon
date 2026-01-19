"""
실버 3
DP

1칸 또는 2칸씩 오르기 가능
연속 3개를 밟으면 안 됨 (2개까지만 연속 가능)
마지막 계단은 반드시 밟아야 함
"""
import sys
input = sys.stdin.readline

N = int(input())
nums = [0, 0] + [int(input()) for _ in range(N)]

dp = [[0] * 2 for _ in range(N + 2)]  # dp[i][0]: 전칸안밟은거, dp[i][1]: 전칸밟은거

for i in range(2, N + 2):
    dp[i][0] = max(dp[i - 2]) + nums[i]
    dp[i][1] = dp[i - 1][0] + nums[i]

print(max(dp[-1]))