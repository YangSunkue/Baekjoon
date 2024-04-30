import sys
input = sys.stdin.readline

# x, y의 길이
N = int(input())
# 추첨번호 입력받기
board = []
for i in range(N):
    board.append(list(map(int, input().split())))


# 시작 좌표와 한 변의 길이 입력받기
def special(x, y, N):

    # 사람이 1명이면 그 사람이 받는다
    if N == 1:
        return board[0][0]
    
    # 사람이 4명이면 번호가 2번째로 작은 사람 고르기
    if N == 2:
        arr = []
        for i in range(x, x + N):
            for j in range(y, y + N):
                arr.append(board[i][j])

        # 정렬 후 2번째로 작은 값 리턴
        arr.sort()
        return arr[1]
    
    # 사람이 4명보다 많을 경우 4명이 될 때까지 나눈다
    else:
        arr = []
        arr.append(special(x, y, N//2))
        arr.append(special(x, y + N//2, N//2))
        arr.append(special(x + N//2, y, N//2))
        arr.append(special(x + N//2, y + N//2, N//2))
        arr.sort()
        return arr[1]


print(special(0, 0, N))