import heapq
import sys
input = sys.stdin.readline

"""
N: 지름길의 개수 (1 ~ 12)
D: 고속도로의 길이 (1 ~ 10000)
graph: 경로 그래프
"""

N, D = map(int, input().split())
graph = [[] for _ in range(D + 1)]  # 경로 그래프

"""기본 경로 추가"""
for i in range(D):
    graph[i].append((1, i + 1))  # i에서 i + 1위치로 1거리로 이동 가능

"""지름길 추가"""
for i in range(N):
    start, end, length = map(int, input().split())

    if end <= D:
        graph[start].append((length, end))  # start에서 end 위치로 length 거리로 이동 가능

"""시작점부터 i까지 최단 거리 리스트"""
result = [float('inf')] * (D + 1)  # inf로 초기화
result[0] = 0  # 시작점은 거리 0

heap = []
heapq.heappush(heap, (0, 0))
while heap:

    cur_cost, cur_pos = heapq.heappop(heap)

    # 이미 계산된 경로보다 먼 경로라면 패스
    if cur_cost > result[cur_pos]:
        continue

    # 현재경로에서 갈 수 있는 모든 경로 검사
    for cost, next_pos in graph[cur_pos]:

        # 시작점부터 다음 노드까지 거리 계산
        next_dist = cur_cost + cost

        # 계산된 경로보다 더 짧다면 갱신하고 큐에 넣기
        if next_dist < result[next_pos]:

            result[next_pos] = next_dist
            heapq.heappush(heap, (next_dist, next_pos))

print(result[-1])