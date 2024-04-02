import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

N = int(input())  # 도시 개수 ( 노드 개수 )
E = int(input())  # 버스 개수 ( 간선 개수 )
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())  # 출발노드, 도착노드, 거리 입력받기
    graph[a].append([c, b])  # (거리, 도착노드)

start, end = map(int, input().split())  # 계산해야 할 출발지, 도착지
distance = [INF] * (N + 1)  # 최단 경로 리스트


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))  # 시작 노드 거리(0)와 시작 노드 큐에 삽입
    distance[start] = 0 # 시작 노드의 최단 경로 초기화

    while queue:
        dist, here = heapq.heappop(queue)  # 큐에서 거리, 노드 빼기
        if distance[here] < dist:  # 기존최단경로가 방금뽑은거리보다 짧다면 패스
            continue

        for i in graph[here]:  # 방금뽑은노드의 인접노드에 대하여 반복
            cost = distance[here] + i[0]  # 방금뽑은거리 + 인접노드까지 거리를 계산
            if cost < distance[i[1]]:  # 계산한게 기존 인접노드까지의 최단경로보다 짧으면 테이블 갱신
                distance[i[1]] = cost
                heapq.heappush(queue, (cost, i[1]))  # 갱신했으니 거리와 노드 큐에 삽입


dijkstra(start)
print(distance[end])  # start부터 end까지의 최단경로 출력