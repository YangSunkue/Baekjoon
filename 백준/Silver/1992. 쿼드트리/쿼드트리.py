n = int(input())  # 변의 길이
board = [list(map(int, input().rstrip())) for _ in range(n)]  # rstrip() 하면 개행문자 제거해서 한번에 입력할 수 있게 해준다

def quadTree(x, y, n):  # x, y좌표와 변 길이를 입력받는다, 첫 호출은 0,0을 입력
    color = board[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):  # 현재 사각형의 모든 칸을 검사한다
            if color != board[i][j]:  # 색깔이 다른 칸이 하나라도 있다면 4등분 재귀호출 한다
                print('(', end='')  # 출력 양식에 맞게 괄호 입력
                quadTree(x, y, n//2)  # 출력 양식에 맞도록 왼위, 오위, 왼아, 오아 차례대로 호출해야 함
                quadTree(x, y+n//2, n//2)
                quadTree(x+n//2, y, n//2)
                quadTree(x+n//2, y+n//2, n//2)
                print(')', end='')  # 하위 함수에서 알아서 값을 return했을거라 믿고 괄호로 닫아준다
                return  # 하위 함수에서 print를 모두 수행했을 테니 return으로 끝낸다
            
    # 모든 색이 같다면
    print(color, end='')

quadTree(0, 0, n)