import sys
input = sys.stdin.readline

board = [list(map(int, input().strip())) for _ in range(9)]

def get_possible(x, y) -> set:
    """board[x][y]에 가능한 숫자 집합을 리턴"""

    possible = set(range(1, 10))

    # 가로 제거
    possible -= set(board[x])

    # 세로 제거
    for i in range(9):
        possible.discard(board[i][y])
    
    # 박스 제거
    for i in range((x // 3) * 3, ((x // 3) * 3) + 3):
        for j in range((y // 3) * 3, ((y // 3) * 3) + 3):
            possible.discard(board[i][j])
    
    return possible



def solve_sudoku():
    """재귀 + 백트래킹으로 보드 채우기"""

    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:

                for value in get_possible(x, y):
                    board[x][y] = value

                    if solve_sudoku():
                        return True
                    
                board[x][y] = 0
                return False
    return True

solve_sudoku()
for i in range(9):
    for j in range(9):
        print(board[i][j], end='')
    print()