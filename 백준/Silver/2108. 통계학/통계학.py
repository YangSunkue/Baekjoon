# 구현, 수학, 정렬
import sys
input = sys.stdin.readline

N = int(input()) # 수의 개수, 홀수
number = []
for _ in range(N):
    number.append(int(input()))

if N == 1: # 수가 1개일 경우
    print(f'{number[0]}\n{number[0]}\n{number[0]}\n0')

else: # 수가 3개 이상일 경우
    number.sort()

    # 최빈값 구하기, 첫번째 숫자 넣어놓고 시작한다
    result = [number[0]]
    curCnt = 1
    maxCnt = 1

    # 리스트를 한번 순회하며 최빈값을 찾는다
    for i in range(1, N):
        
        if number[i] == number[i-1]: # 이전 숫자와 같을 경우 카운트 추가
            curCnt += 1

            if curCnt == maxCnt: # 최빈값이 겹칠 경우 append 한다
                result.append(number[i])

            elif curCnt > maxCnt: # 최빈값이 갱신되었다면 대체한다
                result = [number[i]]
                maxCnt = curCnt
        
        else: # 새로운 숫자일 경우 카운트 초기화
            curCnt = 1

            if curCnt == maxCnt: # 최빈값이 겹칠 경우 append 한다
                result.append(number[i])
    
    
    print(round(sum(number) / N)) # 평균
    print(number[N//2]) # 중앙값
    # 최빈값
    if len(result) > 1:
        result.sort()
        print(result[1])
    else: print(result[0])
    print(number[-1] - number[0]) # 범위