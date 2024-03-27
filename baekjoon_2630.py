import sys

n = int(sys.stdin.readline())  # 종이 길이
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 색깔
result = []   # 결과를 담을 변수

def cut(x, y, n):  # 행, 열 시작지점과 종이 길이를 입력받는다
    color = paper[x][y]  # 종이 색깔 비교를 위한 색깔 저장

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:  # 다른 색깔이 존재할 경우 종이를 4등분한다
                cut(x, y, n//2)
                cut(x+n//2, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y+n//2, n//2)
                return  # 4등분한 하위 함수에서 이미 결과를 제출했을 것이므로 return 한다

    # 종이 색깔이 모두 같다면 result에 결과 담기
    if color == 0:
        result.append(0)
    else:
        result.append(1)

# 함수 실행
cut(0, 0, n)

# 결과 출력
print(result.count(0))
print(result.count(1))