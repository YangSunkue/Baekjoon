"""
골드 3
백트래킹

0: 빈칸
6: 벽
1~5: CCTV (통과 가능)

사각 지대 최소 크기 구하기
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

rooms = []
cctvs = []
initial_blind = 0
for i in range(N):
    row = list(map(int, input().split()))
    rooms.append(row)

    for j in range(M):
        if row[j] == 0:
            initial_blind += 1
        elif 1 <= row[j] <= 5:
            cctvs.append((i, j, row[j]))

watched = [[0] * M for _ in range(N)]
min_blind = float('inf')

# CCTV 번호별 가질 수 있는 방향 조합
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
cctv_modes = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [3, 1], [1, 2], [2, 0]],
    [[2, 0, 3], [0, 3, 1], [3, 1, 2], [1, 2, 0]],
    [[0, 1, 2, 3]]
]

def can_go(nx, ny):
    return 0 <= nx < N and 0 <= ny < M and rooms[nx][ny] != 6

def toggle_explore(x, y, modes, is_exploring):
    """
    is_exploring: True(감시 시작), False(감시 취소)
    감시/해제된 빈칸(0)의 개수를 리턴
    """
    count = 0
    for mode in modes:
        nx, ny = x, y
        while True:
            nx += directions[mode][0]
            ny += directions[mode][1]

            if not can_go(nx, ny):
                break

            if rooms[nx][ny] == 0:
                if is_exploring:
                    if watched[nx][ny] == 0: count += 1
                    watched[nx][ny] += 1
                else:
                    watched[nx][ny] -= 1
                    if watched[nx][ny] == 0: count += 1
    return count

def back_tracking(depth, current_blind):

    global min_blind

    if depth == len(cctvs):
        min_blind = min(min_blind, current_blind)
        return
    
    x, y, num = cctvs[depth]

    for modes in cctv_modes[num]:
        monitored = toggle_explore(x, y, modes, True)
        back_tracking(depth + 1, current_blind - monitored)
        toggle_explore(x, y, modes, False)

back_tracking(0, initial_blind)
print(min_blind)