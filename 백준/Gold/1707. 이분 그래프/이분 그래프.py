import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

# 이분 그래프 판별 DFS 함수
def DFS(graph, start, visited, group): 
    visited[start] = group

    for i in graph[start]:
        if visited[i] == 0:  # 방문 안 한 곳이라면
            result = DFS(graph, i, visited, -group)
            if not result: return False  # 하위에서 이분 그래프 아니라고 판단했다면 함수 종료
        elif visited[i] == group:  # 인접노드인데 그룹이 같을경우 이분그래프 아님
            return False
    return True

# 입력받은 갯수만큼 그래프를 검사한다
for _ in range(int(input())):
    # 사전준비
    N, E = map(int, input().split())  # 노드, 간선
    graph = [[] for _ in range(N + 1)]  # 연결정보
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0 for _ in range(N + 1)]  # 방문체크 리스트

    # 모든 노드에 대하여 DFS 진행
    for i in range(1, N + 1):
        if visited[i] == 0:  # 확인 안 한 노드가 있다면 진행
            result = DFS(graph, i, visited, 1)
            if not result: break
    print("YES") if result else print("NO")  # 이분 그래프면 YES, 아니면 NO 출력
