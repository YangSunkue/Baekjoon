import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def DFS(graph, start, visited, group): # group값으로 그룹을 구분한다
    visited[start] = group

    for i in graph[start]:
        if visited[i] == 0:  # 아직 방문 안 했을 경우
            result = DFS(graph, i, visited, -group)  # 그룹을 바꿔서 재귀호출
            if result == False:  # 하위호출에서 False가 나왔다면 이미 이분 그래프 아니므로 함수 종료시키기
                return False
        else: 
            if visited[i] == group:  # 만약 현재그룹과 같다면 False 리턴( 이분 그래프 아님 )
                return False
    return True  # 이분 그래프라면 True 리턴

for _ in range(int(input())):
    # 사전준비
    N, E = map(int, input().split())  # 노드, 간선
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0 for _ in range(N + 1)]

    # DFS 진행, 그래프가 끊어져 있을 수도 있으므로 가지 않은 노드가 있다면 해당 노드부터 DFS 진행
    for i in range(1, N + 1):
        if visited[i] == 0:
            result = DFS(graph, i, visited, 1)
            if result == False:
                break
    print("YES") if result else print("NO")
