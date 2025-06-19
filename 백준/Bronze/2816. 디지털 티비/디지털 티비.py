import sys
input = sys.stdin.readline

"""
1: 화살표 내리기
2: 화살표 올리기
3: 화살표, 채널 내리기
4: 화살표, 채널 올리기
"""

N = int(input())
channels = [input().strip() for _ in range(N)]

result = ''

KBS1_idx = channels.index('KBS1')
KBS2_idx = channels.index('KBS2')

result += ('1' * KBS1_idx)  # KBS1를 선택하러 1을 누른 횟수
result += ('4' * KBS1_idx)  # KBS1을 0번으로 가져오러 4를 누른 횟수

# KBS2가 KBS1 보다 앞에 있다면, KBS1 이동 중 자리가 바뀌었으므로 1과 4를 한번씩 더 눌러야 한다
if KBS1_idx > KBS2_idx:
    result += ('1' * (KBS2_idx + 1))  # KBS2를 선택하러 1을 누른 횟수
    result += ('4' * (KBS2_idx))  # KBS2을 1번으로 가져오러 4를 누른 횟수
else:
    result += ('1' * KBS2_idx)
    result += ('4' * (KBS2_idx - 1))

print(result)