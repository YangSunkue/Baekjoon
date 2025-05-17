import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(12)] for _ in range(N)]
for i in range(2, len(dp[0]) - 1):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(1, 11):
        
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N-1]) % int(1e9))