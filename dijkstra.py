import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())  # 노드, 간선
start = int(input())  # 시작 노드
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())  # 출발노드, 도착노드, 거리
    graph[a].append([c, b])  # (거리, 노드)
distance = [INF] * (N + 1)  # 최단거리 저장 리스트

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))  # 시작노드 입력하기, 시작노드 거리는 0으로 한다 (거리, 노드)
    distance[start] = 0  # 최단경로 리스트에 시작노드 입력

    while queue:
        dist, here = heapq.heappop(queue)  # 현재노드까지의 최단거리 , 현재노드
        if distance[here] < dist:  # 기존 최단경로가 방금꺼낸 거리보다 작다면 넘겨버린다
            continue

        for i in graph[here]:  # 방금꺼낸 거리가 최단경로라면, 최단경로 + 인접노드까지의 거리를 더해 계산한다
            cost = dist + i[0]  # i[0]은 here노드로부터 인접노드 까지의 거리이다
            if cost < distance[i[1]]:  # 방금 계산한 거리가 최단경로라면 테이블 갱신한다 , i[1]은 노드번호다
                distance[i[1]] = cost
                heapq.heappush(queue, (cost, i[1]))  # 갱신했으니 큐에 삽입한다

dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == INF:
        print("INFINITY", end=' ')
    else:
        print(distance[i], end=' ')



# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2