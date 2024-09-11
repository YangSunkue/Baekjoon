import sys
input = sys.stdin.readline

N = int(input()) # 노드 개수
inout = input().strip()
inout = [''] + [int(x) for x in inout] # 실내여부, 노드번호와 동기화를 위해 맨앞 빈값 추가
graph = [[] for _ in range(N + 1)] # 노드 연결정보, 노드번호와 동기화를 위해 맨앞 빈값 추가
for i in range(N - 1):
    a, b = map(int, input().split()) # 연결된 두 노드
    graph[a].append(b) # 양쪽 노드에 연결정보 추가
    graph[b].append(a)

def dfs(graph, node, visited):

    global result

    if not visited[node] and inout[node] == 1: # 현재 노드가 실내일 경우 길 한개 찾은 것
        visited[node] = True
        result += 1
        return
    
    visited[node] = True
    # 현재 노드가 실외일 경우 방문 안 한 인접 노드들 탐색
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)

result = 0
for i in range(1, N + 1):
    if inout[i] == 1: # 시작 노드가 실내일 경우에만 탐색
        visited = [False] * (N + 1) # 방문목록 초기화
        visited[i] = True
        dfs(graph, i, visited)

print(result)