# 분할 정복
import sys
input = sys.stdin.readline

N = int(input())
start = ['***', '* *', '***'] # N이 3일 경우의 초기 모양

def divideAndConquer(num, star):

    # 종료 조건
    if num == N:
        return star
    
    """
    이 반복문은 기존 star를 그대로 출력하는 것을 의미한다.
    따라서 3배 곱하여 append해주면 옆으로 3배 늘리는 것이 된다.
    for i in range(num):
        print(star[i])
    """

    tmpStar = []
    # 옆으로 3배 늘리는 작업을 3번 반복한다
    for i in range(num):
        tmpStar.append(star[i] * 3)
    
    # 가운데 부분은 공백으로 만든다
    for i in range(num):
        tmpStar.append(star[i] + ' ' * num + star[i])
    
    for i in range(num):
        tmpStar.append(star[i] * 3)
    
    return divideAndConquer(num * 3, tmpStar)

# 정답 출력
result = divideAndConquer(3, start)
for re in result:
    print(re)