"""
실버 3
DP

날짜 + 시간이 N + 1 이하면 상담 가능
"""
import sys
input = sys.stdin.readline

N = int(input())
T = [0] * (N + 1)  # 소요시간
P = [0] * (N + 1)  # 상담비용

for i in range(1, N + 1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

# dp[i]: i일부터 끝까지 얻을 수 있는 최대비용
dp = [0] * (N + 2)  # dp[N + 1] = 0 (퇴사일)

for i in range(N, 0, -1):

    # i일 상담이 퇴사전에 끝나는 경우 상담 진행
    if i + T[i] <= N + 1:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[1])