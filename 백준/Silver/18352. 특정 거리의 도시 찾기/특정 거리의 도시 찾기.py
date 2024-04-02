import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

N, E, K, start = map(int, input().split())  # 노드, 간선, 찾을거리, 출발노드
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b = map(int, input().split())  # 출발노드, 도착노드
    graph[a].append([1, b])  # 거리(1), 도착노드
distance = [INF] * (N + 1)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))  # 시작노드거리, 시작노드 큐에 삽입
    distance[start] = 0  # 시작노드 최단거리 입력

    while queue:
        dist, here = heapq.heappop(queue)
        if distance[here] < dist:  # 기존 최단경로가 지금 가져온 거리보다 짧다면 패스
            continue

        for i in graph[here]: # 현재노드 인접노드정보 가져오기
            cost = dist + i[0]  # 최단거리 + 다음노드까지 거리 계산
            if cost < distance[i[1]]:  # 계산한 게 최단거리라면 최단경로 테이블 갱신
                distance[i[1]] = cost
                heapq.heappush(queue, (cost, i[1]))  # 갱신했으니 큐에 넣기

dijkstra(start)
result = []
for i in range(1, N + 1):
    if distance[i] == K:  # 찾으려는 최단 거리와 일치한다면 결과 리스트에 추가
        result.append(i)

if len(result) == 0:  # 일치하는 노드가 없다면 -1 출력
    print(-1)
else:
    for i in result:
        print(i)