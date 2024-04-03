import heapq
import sys

input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
visited = [False] * (N + 1)

def prim(graph, start):
    visited[start] = True
    distance = 0
    edge = [(cost, start, end) for cost, end in graph[start]]  # 시작노드의 인접노드에 대한 정보를 미리 리스트에 넣는다
    heapq.heapify(edge)  # 리스트를 우선순위 큐(최소힙)로 변경한다.

    while edge:
        cost, start, end = heapq.heappop(edge)
        if visited[end] == False:
            visited[end] = True
            distance += cost

            for nextCost, nextEnd in graph[end]:  # 방금 추가한 노드의 인접 노드에 대하여 반복
                if visited[nextEnd] == False:
                    heapq.heappush(edge, (nextCost, end, nextEnd))

    return distance

print(prim(graph, 1))