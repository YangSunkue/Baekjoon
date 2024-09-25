# 수학, 구현, 정렬
import sys
input = sys.stdin.readline

N = int(input()) # 숫자 개수, 홀수
number = [] # 수 입력받기
for _ in range(N):
    number.append(int(input()))

if N == 1:
    print(f'{number[0]}\n{number[0]}\n{number[0]}\n0')

else:
    number.sort() # 정렬
    # 최빈값 구하기 : 같으면 append하고, 넘었으면 대체한다
    result = [number[0]]
    maxCnt = 1
    curCnt = 1
    for i in range(1, N):
        if number[i] == number[i-1]: # 이전 숫자가 다시 등장했다면
            curCnt += 1 # 카운트 1 증가
            if curCnt == maxCnt: # 최빈값이 겹친다면 append한다
                result.append(number[i])
                maxCnt = curCnt
            elif curCnt > maxCnt: # 최빈값 역전했으면 대체한다
                result = [number[i]]
                maxCnt = curCnt
        
        else: # 다른 숫자가 등장했을 경우 카운트 초기화
            curCnt = 1
            if curCnt == maxCnt: # 최빈값이 겹친다면 append한다
                result.append(number[i])
                maxCnt = curCnt

    print(round(sum(number) / N)) # 평균
    print(number[N//2]) # 중앙값
    if len(result) >= 2:
        result.sort()
        print(result[1]) # 최빈값 ( 2번째로 작은 값 ) 
    else:
        print(result[0]) # 최빈값
    print(number[-1] - number[0]) # 범위