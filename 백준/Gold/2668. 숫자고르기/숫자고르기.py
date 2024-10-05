# DFS
import sys
input = sys.stdin.readline

# 입력받기
N = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i].append(int(input()))

def DFS(cur, start, tmpPath): # 현재노드, 시작노드

    visited[cur] = True
    tmpPath.append(cur)

    for edge in graph[cur]:
        if edge in path: continue # 이미 싸이클에 포함된 노드일 경우 continue

        if not visited[edge]:
            DFS(edge, start, tmpPath)

        elif edge == start:
            for t in tmpPath:
                path.append(t)

# 한 노드가 하나의 사이클에만 포함된다면 path를 저장하고 path에 저장된 정점은 visited와 동일하게 취급해야 함
path = []
for i in range(1, N + 1):
    if i not in path:
        visited = [False] * (N + 1)
        DFS(i, i, [])

path.sort()
print(len(path))
for pa in path:
    print(pa)