import sys
input = sys.stdin.readline

N = int(input()) # 수의 개수
numbers = list(map(int, input().split())) # 수열
M = int(input()) # 구간의 개수

# 누적합 배열 만들기
result = [0 for _ in range(N)]
result[0] = numbers[0]
for i in range(1, N):
    result[i] = result[i-1] + numbers[i]

# 결과 출력
for _ in range(M):

    a, b = map(int, input().split()) # 구간 입력받기

    if a == 1:
        print(result[b-1])
    else:
        print(result[b-1] - result[a-2])