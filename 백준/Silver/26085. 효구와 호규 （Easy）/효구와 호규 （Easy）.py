import sys
input = sys.stdin.readline
INF = int(1e9)

# N, M 입력받기
N, M = map(int, input().split())

# 총 숫자 갯수
count = N * M

# board 입력받으며 0, 1 갯수 세기
zeroCount = 0
oneCount = 0
board = []
for i in range(N):

    a = list(map(int, input().split()))
    board.append(a)

    # 0, 1 갯수 추가
    zeroCount += a.count(0)
# 1갯수는 총 갯수에서 0갯수 뺀 값
oneCount = count - zeroCount

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 한번이라도 삭제되었다면 다 삭제할 수 있는건가?
# 모든 좌표를 돌아봐도 아무것도 삭제할 수 없었다면 -1 인가?
def deleteGo(nx, ny, cx, cy, board):

    # 전역 변수 설정
    global count

    # 다음 좌표가 안에 있고 / 현재카드가 INF 아니고 /  현재 카드와 다음 좌표 숫자가 같으면 지우기
    if 0 <= nx < N and 0 <= ny < M and board[cx][cy] != INF and board[nx][ny] == board[cx][cy]:
        board[cx][cy] = INF
        board[nx][ny] = INF

        # 총 갯수에서 지운 만큼 빼주기
        count -= 2

        # 지웠으면 True 리턴
        return True
    # 못지웠으면 False 리턴
    return False

def killCard():

    # 총 갯수가 홀수일 경우 ( 0, 1 둘중 하나는 무조건 홀수다 )
    if count % 2 == 1:
        return -1

    # 0 또는 1이 홀수일 경우 -1 리턴
    if zeroCount % 2 == 1 or oneCount % 2 == 1:
        return -1
    
    for x in range(N):
        for y in range(M):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                result = deleteGo(nx, ny, x, y, board)

                # 한번이라도 True라면(삭제되었다면)
                if result:
                    return 1
    return -1
            
print(killCard())