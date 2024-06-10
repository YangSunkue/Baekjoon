import sys
import itertools
input = sys.stdin.readline

# 질문 횟수
N = int(input())

# 숫자, 스트라이크, 볼
q = []
for i in range(N):
    q.append(list(map(int, input().split())))

num = [i for i in range(1, 10)]
numbers = list(itertools.permutations(num, 3))

# 결과 저장할 변수
result = 0
# 생성된 모든 숫자에 대해서 반복
for i in numbers:
    

    # 숫자 하나하나에 대해, 모든 질문에 대한 조건 검사
    for j in range(len(q)):
        strike = 0
        ball = 0

        for k in range(3):
            if str(i[k]) == str(q[j][0])[k]:  # 숫자가 일치하면 strike
                strike += 1
            elif str(q[j][0])[k] in str(i):  # 일치하진 않지만 존재하면 ball
                ball += 1
        
        # strike나 ball 중 하나라도 맞지 않는다면 break ( 다음 숫자 보러 간다 )
        if strike != q[j][1] or ball != q[j][2]:
            break

        # 마지막 반복일 경우
        # 즉, 하나의 숫자가 모든 조건을 통과했을 경우
        if j == (len(q) - 1):
            result += 1

print(result)