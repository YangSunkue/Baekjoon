# 분할 정복
import sys
input = sys.stdin.readline

N = int(input())

start = ['***', '* *', '***']  # N = 3일 경우 별 초기화

def divideAndConquer(num, star):
    
    # 종료조건
    if num == N:
        return star
    
    # 별 모양을 늘린다
    tmpStar = []
    # 아래로 3배
    for i in range(num):
        tmpStar.append(star[i] * 3) # 옆으로 3배

    # 아래로 3배
    for i in range(num):
        tmpStar.append(star[i] + ' ' * num + star[i]) # 옆으로 3배
        
    # 아래로 3배
    for i in range(num):
        tmpStar.append(star[i] * 3) # 옆으로 3배
    
    return divideAndConquer(num * 3, tmpStar)


result = divideAndConquer(3, start)
for re in result:
    print(re)