import sys
sys.setrecursionlimit(10 ** 9)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]  # 노드번호와 인덱스번호를 맞추기 위해 + 1
for _ in range(M):
    root, edge = map(int, sys.stdin.readline().split())
    graph[root].append(edge)
    graph[edge].append(root)

visited = [False] * (N + 1)  # 노드번호와 인덱스번호를 맞추기 위해 + 1
visited[0] = True  # 모든 노드에 들렸는지 편하게 확인하기 위해 안쓰는 0번을 True로 초기화해준다
conn = 0

def dfs(graph, v, visited):
    visited[v] = True  # 들렸으니 방문처리

    for i in graph[v]:  # 인접 노드 순회하기
        if visited[i] == False:  # 인접노드 안들렸을경우
            dfs(graph, i, visited)

while False in visited:  # False가 하나라도 있다면 반복문 진행(연결 요소가 2개 이상 있다고 판단)
    start = visited.index(False)  # 들리지 않은 노드를 시작 노드로 설정
    dfs(graph, start, visited)  # dfs 돌리기
    conn += 1 # 한번 돌릴때마다 연결 요소 1개씩 증가

print(conn)  # 계산된 연결 요소 개수 출력