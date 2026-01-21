"""
골드 5
그리디
"""
import sys
input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort(key=lambda x: (x[0], x[1]))

cur_start = lines[0][0]
cur_end = lines[0][1]
total_length = 0

for i in range(1, N):
    next_start, next_end = lines[i]

    # 선이 겹치거나 이어지면 끝점만 확장
    if next_start <= cur_end:
        cur_end = max(cur_end, next_end)
    
    # 선이 끊어지면 기존 선 정산하고 새로 시작
    else:
        total_length += (cur_end - cur_start)
        cur_start = next_start
        cur_end = next_end

total_length += (cur_end - cur_start)
print(total_length)