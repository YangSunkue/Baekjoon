"""
실버 3
DP

날짜 + 시간이 N + 1 이하면 상담 가능
"""
import sys
input = sys.stdin.readline

N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)

for i in range(1, N + 1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

dp = [0] * (N + 2)
for i in range(N, 0, -1):
    if i + T[i] <= N + 1:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[1])