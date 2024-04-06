# 0을 만드는 경우의 수는 동전 종류가 무엇이든 무조건 1개가 존재한다.
# DP[money][coin] = DP[money-coin][coin]
# 다음 동전을 계산할 땐 윗줄(이전동전)의 값을 받고 시작한다
# money : 목표금액 / coin : 현재동전
# money : 가로(x행의 y값) / coin : 세로 (y열의 x값)

import sys


input = sys.stdin.readline

T = int(input())  # 테스트 케이스 개수

for _ in range(T):  # 테스트 케이스 개수만큼 진행한다
    N = int(input())  # 동전 종류 개수
    coinBox = list(map(int, input().split()))  # 동전 입력받기
    coinBox.insert(0, 0)  # 0번 인덱스에 0넣기. 첫번째 동전부터 공식을 적용하기 위함.
    money = int(input())

    dp = [[0] * (money + 1) for i in range(N + 1)]  # 목표금액만큼 한 행을 길게, 동전갯수만큼 한 열을 길게
    for i in range(N + 1):
        dp[i][0] = 1  # 동전이 뭐든 간에 0을 만드는 경우의 수는 항상 1

    for x in range(1, N + 1):  # 동전 종류만큼 반복
        for y in range(1, money + 1):  # 각 동전 당 목표금액까지 반복한다
            dp[x][y] = dp[x-1][y]
            if y-coinBox[x] >= 0:
                dp[x][y] += dp[x][y-coinBox[x]]

    print(dp[N][money])