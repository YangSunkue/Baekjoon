import heapq
import sys
input = sys.stdin.readline

N, D = map(int, input().split())

"""각 노드의 경로 저장 (거리, 다음위치)"""
graph = [[] for _ in range(D + 1)]

# 기본 경로
for i in range(D):
    graph[i].append((1, i + 1))

# 지름길
for i in range(N):
    start, end, cost = map(int, input().split())

    if end <= D:
        graph[start].append((cost, end))

"""다익스트라"""
result = [float('inf')] * (D + 1)  # 최단거리 리스트
result[0] = 0  # 시작지점 거리는 0
heap = []  # 최소힙 사용
heapq.heappush(heap, (0, 0))
while heap:

    cur_cost, cur_pos = heapq.heappop(heap)

    # 뽑은 거리가 이미 계산된 경로보다 길면 패스
    if cur_cost > result[cur_pos]:
        continue

    for cost, next_pos in graph[cur_pos]:

        # 다음 위치까지의 거리 계산
        next_cost = cur_cost + cost

        # 이미 계산된 경로보다 짧을 경우 최단거리 갱신, 힙에 넣기
        if next_cost < result[next_pos]:

            result[next_pos] = next_cost
            heapq.heappush(heap, (next_cost, next_pos))

print(result[-1])