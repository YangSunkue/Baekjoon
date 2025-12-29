import sys
input = sys.stdin.readline

"""
N - LIS 길이
"""

N = int(input())
kids = [201] + [int(input()) for _ in range(N)]

dp = [1] * (N + 1)
for i in range(2, N + 1):
    for j in range(1, i):
        if kids[i] > kids[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))