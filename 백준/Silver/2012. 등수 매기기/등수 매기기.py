"""
실버 3
그리디
"""
import sys
input = sys.stdin.readline

N = int(input())

ranking = [int(input()) for _ in range(N)]
ranking.sort()

result = 0
for i in range(1, N + 1):
    result += abs(ranking[i - 1] - i)

print(result)