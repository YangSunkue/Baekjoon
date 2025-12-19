import sys
input = sys.stdin.readline

N = int(input())
MOD = 1_000_000_000

dp = [[[0] * 1024 for _ in range(10)] for _ in range(N + 1)]
for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(1, N):
    for j in range(10):
        for mask in range(1024):

            if dp[i][j][mask] == 0:
                continue

            if j > 0:
                new_mask = mask | (1 << (j - 1))
                dp[i + 1][j - 1][new_mask] = (dp[i + 1][j - 1][new_mask] + dp[i][j][mask]) % MOD
            
            if j < 9:
                new_mask = mask | (1 << (j + 1))
                dp[i + 1][j + 1][new_mask] = (dp[i + 1][j + 1][new_mask] + dp[i][j][mask]) % MOD

result = 0
for i in range(10):
    result = (result + dp[N][i][1023]) % MOD

print(result)