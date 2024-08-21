import copy
import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))

dp = copy.deepcopy(numList)
for i in range(1, N):
    for j in range(i):
        if numList[i] > numList[j]:
            dp[i] = max(dp[i], dp[j] + numList[i])

print(max(dp))