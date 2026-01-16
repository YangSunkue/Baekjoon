"""
실버 5
DP
"""
import sys
input = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]  # dp[x][y] = x개 중에서 y개 뽑는 경우의 수

for x in range(31):
    dp[x][0] = 1
    dp[x][x] = 1

for x in range(2, 31):
    for y in range(1, x):
        dp[x][y] = dp[x - 1][y - 1] + dp[x - 1][y]

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(dp[M][N])