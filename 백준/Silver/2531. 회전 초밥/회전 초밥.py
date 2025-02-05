# 실버1 -> 투 포인터
"""
N : 회전 초밥 벨트에 놓인 접시의 수
D : 초밥의 가짓수(초밥 최대 번호)
K : 연속해서 먹어야 하는 접시의 수
C : 쿠폰으로 먹을 수 있는 초밥 번호

(인덱스 % 리스트 길이) 사용하면 원형 리스트 구현 가능
"""

import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

count = 0
for start in range(len(sushi)):
    
    choice = [sushi[(start + i) % N] for i in range(K)]
    unique_choice = set(choice)
    unique_choice_length = len(unique_choice)

    # 쿠폰 사용
    if C not in choice: unique_choice_length += 1

    # 결과 갱신
    count = max(unique_choice_length, count)

print(count)