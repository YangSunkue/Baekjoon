import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 노드번호와 인덱스 번호를 맞추기 위해서 + 1하여 INF로 초기화
for a in range(1, n + 1):  # 자기 자신으로 가는 비용은 0 으로 초기화
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):  # 간선 정보 입력받기, 인접 행렬 형태
    a, b, c = map(int, input().split())  # 출발, 도착, 비용
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])  # 현재 값과 k를 거쳐가는 값 중 더 작은 값을 선택

for a in range(1, n + 1):
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