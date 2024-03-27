import sys

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = []

def cut(x, y, n):  # 종이 시작좌표와 종이 길이를 받는다
    color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]: # 색이 다른 종이가 있다면 나누기
                cut(x, y, n//2) # 좌표를 변경하고, 종이 길이는 반으로 줄인다
                cut(x+n//2, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y+n//2, n//2)
                return # 결과 append는 하위 함수에서 해줄 것이기 때문에 return해도 된다
    
    if color == 0:
        result.append(0)
    else:
        result.append(1)

cut(0, 0, n)
print(result.count(0))
print(result.count(1))