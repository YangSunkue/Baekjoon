import heapq
import sys

input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())  # 출발, 도착, 비용
    graph[a].append((c, b))
    graph[b].append((c, a))

visited = [False] * (N + 1)
distance = 0
def prim(graph, start):  # 그래프, 시작노드 입력받기
    global distance

    mst = []
    visited[start] = True

    edges = [(cost, start, end) for cost, end in graph[start]]
    heapq.heapify(edges)

    while edges:
        cost, start, end = heapq.heappop(edges)

        if visited[end] == False:
            visited[end] = True
            mst.append((start, end, cost))
            distance += cost

            for nextCost, nextEnd in graph[end]:
                if visited[nextEnd] == False:
                    heapq.heappush(edges, (nextCost, end, nextEnd))
    
    return mst

prim(graph, 1)
print(distance)