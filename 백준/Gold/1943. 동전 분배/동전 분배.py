"""
골드 2
DP, 배낭 문제
"""
import sys
input = sys.stdin.readline

for _ in range(3):

    coins = []
    total = 0

    N = int(input())
    for _ in range(N):
        coin, count = map(int, input().split())
        coins.append((coin, count))
        total += coin * count
    
    if total % 2 == 1:
        print(0)
        continue

    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for coin, count in coins:
        for i in range(target, -1, -1):
            if dp[i]:
                for use in range(1, count + 1):
                    if i + (coin * use) <= target:
                        dp[i + (coin * use)] = True
                    else:
                        break

        if dp[target]: break
        
    print(1 if dp[target] else 0)