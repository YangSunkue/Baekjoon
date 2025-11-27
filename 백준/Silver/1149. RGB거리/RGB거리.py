import sys
input = sys.stdin.readline

"""
1 2 1 2 1 2
이전집과 같지만않으면 되는듯?
"""

N = int(input())
money = []
for _ in range(N):
    money.append(list(map(int, input().split())))

# 빨강 초록 파랑
dp = [[0] * 3 for _ in range(N)]
dp[0][0] = money[0][0]
dp[0][1] = money[0][1]
dp[0][2] = money[0][2]

for i in range(1, N):
    dp[i][0] = money[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = money[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = money[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[-1][0], dp[-1][1], dp[-1][2]))