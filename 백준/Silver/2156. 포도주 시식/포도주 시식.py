"""
실버 1
DP

2잔까지만 연속으로 마실 수 있다
"""
N = int(input())
wine = [0, 0] + [int(input()) for _ in range(N)]

"""
dp[i][0]: 이번 포도주 안마신거
dp[i][1]: 이번꺼 마시고 이전 포도주 안마신거
dp[i][2]: 이번꺼 마시고 이전 포도주 마신거
"""
dp = [[0] * 3 for _ in range(N + 2)]

for i in range(2, N + 2):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = dp[i - 1][0] + wine[i]
    dp[i][2] = dp[i - 1][1] + wine[i]

print(max(dp[-1]))