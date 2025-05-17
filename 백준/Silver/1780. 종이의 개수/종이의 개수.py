import sys
input = sys.stdin.readline

# 분할 함수 : 같은 수로 되어있는지 체크, 아닐경우 분할, 맞다면 -1/0/1 카운트 올리기
# 같은 수로만 되어 있지 않다면 9분할

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

minus, zero, plus = 0, 0, 0

def divide_and_conquer(x, y, length):

    global minus, zero, plus

    prev = data[x][y]
    for i in range(x, x + length):
        for j in range(y, y + length):
            if data[i][j] != prev:
                
                le = length // 3

                divide_and_conquer(x, y, le)
                divide_and_conquer(x + le, y, le)
                divide_and_conquer(x + le*2, y, le)
                divide_and_conquer(x, y + le, le)
                divide_and_conquer(x + le, y + le, le)
                divide_and_conquer(x + le*2, y + le, le)
                divide_and_conquer(x, y + le*2, le)
                divide_and_conquer(x + le, y + le*2, le)
                divide_and_conquer(x + le*2, y + le*2, le)
                return
    
    if prev == -1: minus += 1
    elif prev == 0: zero += 1
    else: plus += 1

divide_and_conquer(0, 0, N)
print(minus)
print(zero)
print(plus)