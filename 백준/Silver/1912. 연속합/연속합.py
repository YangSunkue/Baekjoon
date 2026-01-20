"""
실버 2
DP
"""
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [0] * N  # dp[i]: 0 ~ i까지의 i를 포함하는 최대 연속합
dp[0] = nums[0]

for i in range(1, N):
    dp[i] = max(dp[i - 1] + nums[i], nums[i])

print(max(dp))