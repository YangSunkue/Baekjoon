import sys
input = sys.stdin.readline

dp = [[0] * 4 for _ in range(10001)]
dp[1][1], dp[1][2], dp[1][3] = 1, 1, 1
dp[2][1], dp[2][2], dp[2][3] = 1, 2, 2
dp[3][1], dp[3][2], dp[3][3] = 1, 2, 3

for i in range(4, 10001):
    dp[i][1] = 1

    for j in range(2, 4):
        dp[i][j] = dp[i][j - 1] + dp[i - j][j]

for _ in range(int(input())):
    print(dp[int(input())][3])