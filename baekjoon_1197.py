import heapq
import sys

input = sys.stdin.readline
N, E = map(int, input().split())  # 노드, 간선
graph = [[] for _ in range(N + 1)]  # 그래프 입력받기
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

visited = [False] * (N + 1)  # 방문체크 리스트

def prim(graph, start):  # 그래프, 시작노드 입력받는다, 프림 알고리즘 사용
    visited[start] = True  # 시작노드 방문체크
    distance = 0  # 거리(가중치)를 계산할 변수
    edge = [(cost, start, end) for cost, end in graph[start]]  # 시작노드의 인접노드에 대한 정보를 미리 리스트에 넣는다
    heapq.heapify(edge)  # 리스트를 우선순위 큐(최소힙)로 변경한다.
 
    while edge:  # 큐가 빌 때까지 진행( 모든 노드를 방문할 때까지 )
        cost, start, end = heapq.heappop(edge)  # 큐에서 가중치(거리) 가장 작은 값을 뺀다
        if visited[end] == False:  # 아직 안 간 곳이면
            visited[end] = True  # 방문체크
            distance += cost  # 거리 추가

            for nextCost, nextEnd in graph[end]:  # 방금 추가한 노드의 인접 노드에 대하여 반복
                if visited[nextEnd] == False:  # 안간 곳 있으면 큐에 추가하기
                    heapq.heappush(edge, (nextCost, end, nextEnd))

    return distance  # 계산된 최단거리 리턴

print(prim(graph, 1))