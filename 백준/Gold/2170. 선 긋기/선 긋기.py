"""
골드 5
그리디
"""
import sys
input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()

cur_start = lines[0][0]
cur_end = lines[0][1]
total = 0

for i in range(1, N):

    next_start = lines[i][0]
    next_end = lines[i][1]

    if next_start <= cur_end:
        cur_end = max(cur_end, next_end)
    else:
        total += (cur_end - cur_start)
        cur_start = next_start
        cur_end = next_end

total += (cur_end - cur_start)
print(total)