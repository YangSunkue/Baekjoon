# 실버2 -> 분할 정복, 재귀
"""
N : 1 또는 3의 k승

-1, 0, 1 로 이루어진 N * N 행렬
하나의 수로 이루어져 있지 않다면 9개로 분할
분할을 마친 후, 각 숫자로 이루어진 종이가 몇개인지 출력
"""

import sys
input = sys.stdin.readline

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

minus, zero, plus = 0, 0, 0
def divide(x, y, n):

    global minus, zero, plus

    prev = table[x][y] # 기준이 될 숫자 설정
    for i in range(x, x + n):
        for j in range(y, y + n):
            current = table[i][j]
            if prev != current: # 단일 숫자가 아닐 경우 9개 분할
                ne = n // 3
                divide(x, y, ne)
                divide(x + ne, y, ne)
                divide(x + ne*2, y, ne)
                divide(x, y + ne, ne)
                divide(x, y + ne*2, ne)
                divide(x + ne, y + ne, ne)
                divide(x + ne, y + ne*2, ne)
                divide(x + ne*2, y + ne, ne)
                divide(x + ne*2, y + ne*2, ne)

                return

    # 분할되지 않은 경우, 맞는 count 올리고 return
    if prev == -1:
        minus += 1
    elif prev == 0:
        zero += 1
    else: plus += 1

divide(0, 0, N)
print(minus)
print(zero)
print(plus)