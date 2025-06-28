import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

"""슬라이딩 윈도우"""
result = [sum(visitors[0:X]), 1]  # 결과 저장 [최대방문자, 개수]
prev = sum(visitors[0:X])  # 이전 값 저장
left = 1
right = X
while right < len(visitors):

    # 왼쪽 값을 빼고 다음 값 더하기 (범위 이동)
    count = prev - visitors[left-1] + visitors[right]
    
    if count == result[0]:
        result[1] += 1
    
    elif count > result[0]:
        result[0] = count
        result[1] = 1
    
    prev = count
    left += 1
    right += 1

if result[0] == 0:
    print('SAD')
else:
    print(result[0])
    print(result[1])