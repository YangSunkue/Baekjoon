import sys
input = sys.stdin.readline

"""
N - LIS 길이
"""

N = int(input())
kids = [int(input()) for _ in range(N)]

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if kids[i] > kids[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))