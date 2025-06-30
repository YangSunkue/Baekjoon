import sys
input = sys.stdin.readline

"""
DFS 완전탐색
N: 행 (2 ~ 6)
M: 열 (2 ~ 6)
road: 길과 연료 소모량이 담긴 2차원 리스트

같은 방향으로 연속으로 움직일 수 없음. ( 이전 방향값 저장? )
모든 경우의 수를 다 만들고, 최소연료값 갱신 ( 백트래킹 가지치기도 가능할듯 )
"""

"""유효한 길인지 확인한다"""
def can_go(x, y):
    if 1 <= x < N and 0 <= y < M:
        return True
    return False

"""첫번째 칸 연료를 포함한, 달까지 가는 모든 연료 경우의 수를 구한다"""
def dfs(depth, prev_y, prev_direction, fuel):

    global min_fuel

    # 이미 최소 연료량보다 많다면 리턴 ( 가지치기 )
    if fuel >= min_fuel:
        return

    if depth >= N:
        min_fuel = min(min_fuel, fuel)
        return
    
    # 3방향 진행
    for direction in range(-1, 2, 1):
        # 같은 방향 연속이 아님 and 갈 수 있는 길
        if direction != prev_direction and can_go(depth, prev_y + direction):

            current_y = prev_y + direction
            current_fuel = roads[depth][current_y]

            fuel += current_fuel
            dfs(depth + 1, current_y, direction, fuel)
            fuel -= current_fuel

N, M = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(N)]

min_fuel = int(1e9)
for i in range(M):
    dfs(1, i, 532454, roads[0][i])  # 532454는 의미없는 수, 첫번째 경로와 방향 겹치지 않게 하기 위함

print(min_fuel)