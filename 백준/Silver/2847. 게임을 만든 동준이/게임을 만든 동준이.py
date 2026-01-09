"""
실버 4
그리디
"""
import sys
input = sys.stdin.readline

N = int(input())
levels = [int(input()) for _ in range(N)]

result = 0
for i in range(N - 1, 0, -1):
    if levels[i - 1] >= levels[i]:
        result += levels[i - 1] - levels[i] + 1
        levels[i - 1] = levels[i] - 1

print(result)