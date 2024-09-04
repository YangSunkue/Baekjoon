# 정사각형 한 변의 길이 : 2, 4, 8 ....
import sys
input = sys.stdin.readline

# 2의 N승 크기, R행 C열
N, R, C = map(int, input().split())

# 행/열이 길이 나누기 2이상이면 -> 행 : 아래쪽 사분면/ 열 : 오른쪽 사분면
le = 2**N
# 결과값 편하게 더하기 위해 만든 배열
num = [[0,1], [2,3]]

# 각사분면 0,0값, 변길이, 행, 열
def devide(z, le, row, col):

    if le == 2: # 2*2 정사각형 도달 시
        print(z + num[row][col])
        return

    plus = (le * le) // 4 # 각 사분면 0,0 값의 차이
    half = le // 2
    if row >= half:
        if col >= half:
            # 우측아래 사분면
            devide(z+(plus*3), half, row-half, col-half)
        else:
            # 좌측아래 사분면
            devide(z+(plus*2), half, row-half, col)
    elif col >= half:
        # 우측위 사분면
        devide(z+plus, half, row, col-half)
    else:
        # 좌측위 사분면
        devide(z, half, row, col)

devide(0, le, R, C)