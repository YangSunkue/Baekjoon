import sys
input = sys.stdin.readline

# 함수 영역

## x축 확인 ("-"가 얼마나 이어져 있는지)
def dfs_x(a, b):
    visit[a][b] = True
    stack = [(a, b)]

    while stack:
        x, y = stack.pop()

        if 0 <= y+1 < m and not visit[x][y+1] and table[x][y+1] == "-":
            stack.append((x, y+1))
            visit[x][y+1] = True

## y축 확인 ("|"가 얼마나 이어져 있는지)
def dfs_y(a, b):
    visit[a][b] = True
    stack = [(a, b)]

    while stack:
        x, y = stack.pop()

        if 0 <= x+1 < n and not visit[x+1][y] and table[x+1][y] == "|":
            stack.append((x+1, y))
            visit[x+1][y] = True

# main
n, m = map(int, input().split())
table = [list(input().strip()) for _ in range(n)]
visit = [[False]*m for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            if table[i][j] == "-":
                dfs_x(i, j)
            else:
                dfs_y(i, j)
            answer += 1