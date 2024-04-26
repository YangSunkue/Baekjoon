import sys
input = sys.stdin.readline

N = int(input())
target = int(input())

board = [[0] * N for _ in range(N)]
result = []


# 첫 좌표
x = N // 2
y = N // 2
# 첫 수는 먼저 입력해 둔다
board[x][y] = 1
num = 2
for i in range(1, N):

    # i가 홀수일 때, x는 줄어들고 y는 늘어난다
    if i % 2 == 1:
        for _ in range(1, i + 1):
            x -= 1
            board[x][y] = num
            num += 1    
        for _ in range(1, i + 1):
            y += 1
            board[x][y] = num
            num += 1
    
    # i가 짝수일 때, x는 늘어나고 y는 줄어든다
    else:
        for _ in range(1, i + 1):
            x += 1
            board[x][y] = num
            num += 1    
        for _ in range(1, i + 1):
            y -= 1
            board[x][y] = num
            num += 1
    
    # 마지막 반복엔 x를 한번 더 빼준다
    if i == N - 1:
        for _ in range(1, i + 1):
            x -= 1
            board[x][y] = num
            num += 1

for i in range(N):
    for j in range(N):
        print(board[i][j], end=' ')
        if board[i][j] == target:
            result.append(i + 1)
            result.append(j + 1)
    print()

print(result[0], result[1])