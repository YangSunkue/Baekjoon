# BFS 방식
from collections import deque
import sys

N = int(sys.stdin.readline())
E = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
for i in range(E):
    root, edge = map(int,sys.stdin.readline().split())
    graph[root].append(edge)
    graph[edge].append(root)
for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        # 출력 할 필요 없으니 패스

        for i in graph[v]:  # 방금 꺼낸 노드의 인접 노드 방문여부 체크하고 안갔으면 큐에 넣고 방문처리
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)
print(visited.count(True) - 1)



# DFS 방식
# import sys

# N = int(sys.stdin.readline())  # 노드의 개수
# E = int(sys.stdin.readline())  # 간선의 개수

# graph = [[] for _ in range(N + 1)]  # 노드번호와 동기화 하기 위해 N + 1
# for _ in range(E):
#     root, edge = map(int, sys.stdin.readline().split())  # [1,2] 형태로 입력된다. 1번과 2번에 연결되어 있다는 뜻
#     graph[root].append(edge)  # 무방향(양방향) 그래프이기 때문에 대칭되게 입력해 준다
#     graph[edge].append(root)

# for i in range(1, N + 1):  # 키가 작은 노드부터 가야 하기 때문에 인접 노드 리스트를 정렬한다
#     graph[i].sort

# visited = [False] * (N + 1)  # 노드번호와 동기화 하기 위해 N + 1

# def dfs(graph, v, visited):
#     visited[v] = True  # 왔으니 방문체크
#     # 출력은 할필요 없으니 패스

#     for i in graph[v]:  # 현재 노드의 인접 노드로 가자
#         if visited[i] == False:  # 인접 노드 아직 안 갔다면 가기
#             dfs(graph, i, visited)

# dfs(graph, 1, visited)
# print(visited.count(True) -1)  # 감염된 컴퓨터 수가 아니라, 1번에 의해 감염된 컴퓨터 수