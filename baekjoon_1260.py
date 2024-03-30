from collections import deque
import sys

def DFS(graph, v, visited):  # 인접노드리스트, 시작 노드, 방문목록
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:  # 현재 노드의 인접 노드로 재귀
        if visited[i] == False:  # 아직 안 갔으면 가기
            DFS(graph, i, visited)

def BFS(graph, start, visited):  # 인접노드리스트, 시작 노드, 방문목록
    queue = deque([start])  # 큐에 시작 노드 넣기
    visited[start] = True

    while queue:
        v = queue.popleft()  # 큐에서 노드 빼고 출력
        print(v, end=' ')
        
        for i in graph[v]:  # 뺀 노드의 인접 노드 중 아직 가지 않은 노드 큐에 추가하고 방문 체크
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, sys.stdin.readline().split())  # 노드 개수, 간선 개수, 시작 노드

graph = [[] for _ in range(n + 1)]  # 노드 번호와 인덱스 번호를 맞추기 위해 + 1
for _ in range(m):
    root, edge = map(int, sys.stdin.readline().split())
    graph[root].append(edge)  # root번 인덱스에, root번과 연결된 노드를 추가한다
    graph[edge].append(root)  # 무방향(양방향) 그래프 이므로 양쪽 모두에 추가해준다
for i in range(1, n + 1):  # 각 노드 별 연결 간선 리스트를 정렬한다 ( 작은 노드부터 방문해야 하므로 )
    graph[i].sort()

visited = [False] * (n + 1)  # 노드 번호와 인덱스 번호를 맞추기 위해 + 1

DFS(graph, v, visited)
print()
visited = [False] * (n + 1)  # dfs 실행 후 방문목록 초기화
BFS(graph, v, visited)