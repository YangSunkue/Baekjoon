import sys
sys.setrecursionlimit(10 ** 9)  # 재귀함수 최대깊이 늘려놓기

N, M = map(int, sys.stdin.readline().split())  # 노드개수, 간선개수

graph = [[] for _ in range(N + 1)]  # 노드번호와 인덱스를 맞추기 위해 + 1
for _ in range(M):  # 연결정보 입력받기
    root, edge = map(int, sys.stdin.readline().split())
    graph[root].append(edge)
    graph[edge].append(root)

visited = [False] * (N + 1)  # 노드번호와 인덱스를 맞추기 위해 + 1
visited[0] = True  # 마지막에 False 존재 여부를 검사하기 위해 미리 안쓰는 0번 인덱스도 True로 초기화 해놓음
conn = 0  # 연결 요소 갯수 세는 변수

def dfs(graph, v, visited):  # dfs탐색 시작
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

while False in visited:  # 만약 탐색했는데 안간곳이 있었다 -> 연결 요소가 추가로 있다 -> 안간 노드를 시작으로 dfs 한번 더
    start = visited.index(False)
    dfs(graph, start, visited)
    conn += 1  # 한번 탐색할 때마다 연결요소 + 1

print(conn)  # 계산된 연결요소 개수 출력