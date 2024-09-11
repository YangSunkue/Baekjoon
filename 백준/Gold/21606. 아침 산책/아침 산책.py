import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input()) # 노드 개수
inout = '0' + input() # 실내여부, 노드번호와 동기화를 위해 맨앞 빈값 추가
graph = [[] for _ in range(N + 1)] # 노드 연결정보, 노드번호와 동기화를 위해 맨앞 빈값 추가

result = 0
for _ in range(N - 1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

    if inout[a] == '1' and inout[b] == '1': # 연결된 두 노드가 실내일 경우 경로 2개 추가
        result += 2

visited = [False] * (N + 1)
def dfs(node):

    visited[node] = True
    count = 0
    for i in graph[node]:
        if inout[i] == '1': # 인접 노드가 실내일 경우 count 추가
            count += 1

        elif not visited[i] and inout[i] == '0': # 인접 노드가 방문 안한 실외일 경우 dfs 재귀호출
            count += dfs(i)
    
    return count

# 실외 노드를 기준으로 dfs 진행
# 경로의 수 : 실외 노드의 인접 실내 노드 개수를 num이라고 했을 때 num * (num - 1) 이다.
for i in range(1, N + 1):
    if not visited[i] and inout[i] == '0':
        num = dfs(i)
        result += num * (num - 1)

print(result)