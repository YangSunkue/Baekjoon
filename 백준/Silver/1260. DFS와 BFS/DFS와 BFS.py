from collections import deque  # bfs를 위한 덱 import
import sys

def bfs(graph, start, visited):
    queue = deque([start])  # 큐에 시작 노드 넣기
    visited[start] = True  # 넣었으니 방문처리

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:  # 꺼낸 노드의 인접 노드를 큐에 추가 + 방문처리
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:  # 현재 노드의 인접 노드 순회
        if visited[i] == False:
            dfs(graph, i, visited)


n, m, v = map(int, sys.stdin.readline().split())  # 노드의 개수, 간선 개수, 시작 노드
graph = [[] for _ in range(n + 1)]  # 인덱스 번호와 맞추기 위해 + 1
visited = [False] * (n + 1)  # 인덱스 번호와 맞추기 위해 + 1

for _ in range(m):  # 간선 개수만큼 반복해서 입력받는다
    root, edge = map(int, sys.stdin.readline().split())  # 출발지, 도착지
    graph[root].append(edge)  # 무방향 그래프이므로 양방향 모두 추가해준다
    graph[edge].append(root)


for i in range(1, n + 1):  # 각 노드에 연결된 간선 리스트 정렬
    graph[i].sort()

dfs(graph, v, visited)
print()
visited = [False] * (n + 1)  # 방문목록 초기화
bfs(graph, v, visited)