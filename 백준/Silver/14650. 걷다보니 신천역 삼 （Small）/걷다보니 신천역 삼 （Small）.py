import sys
input = sys.stdin.readline

# 0,1,2 만 가지고 N자리 3의 배수 만들기
# 숫자는 중복 사용할 수 있음
# 시작 숫자는 1 또는 2

N = int(input())

cnt = 0

def backTracking(depth, num):

    global cnt

    # 최대 깊이에 도달했을 경우
    if depth == N:
        # num이 3의 배수면 cnt += 1
        if int(num) % 3 == 0:
            cnt += 1
        return
    
    # 첫 번째 자리라면 1, 2만 넣기
    if num == '':
        for i in range(1, 3):
            backTracking(depth + 1, num + str(i))

    # 아니라면 0, 1, 2 넣기
    else:
        for i in range(3):
            backTracking(depth + 1, num + str(i))
    
backTracking(0, '')
print(cnt)