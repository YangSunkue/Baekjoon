import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 노드번호와 인덱스를 맞추기 위해 n + 1, INF로 초기화
for a in range(1, n + 1): # 자기 자신을 향하는 경로는 0으로 초기화
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):  # 간선 정보 입력받기
    a, b, c = map(int, input().split())
    graph[a][b] = c

###### 플로이드 워셜 알고리즘 #######
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
###### 플로이드 워셜 알고리즘 ######

for a in range(1, n + 1):  # 결과 출력
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2