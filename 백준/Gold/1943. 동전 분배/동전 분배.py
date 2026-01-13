"""
골드 2
DP
"""
import sys
input = sys.stdin.readline

for _ in range(3):

    coins = []
    total = 0

    N = int(input())
    for _ in range(N):
        coin, count = map(int, input().split())
        coins.append([coin, count])
        total += (coin * count)

    if total % 2 == 1:
        print(0)
        continue

    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for coin, count in coins:
        for i in range(target, -1, -1):
            if dp[i]:
                for k in range(1, count + 1):
                    if i + (coin * k) <= target:
                        dp[i + (coin * k)] = True
                    else:
                        break
    
    print(1) if dp[target] else print(0)