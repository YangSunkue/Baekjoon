import sys

N, K = map(int, input().split())  # 물건 수, 버틸 수 있는 무게
item = [[]]  # 물건 입력받기 (무게, 가치)
for _ in range(N):
    item.append(list(map(int, input().split())))

dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]  # dp테이블 만들기, 0행과 0열은 0으로 채우기

for x in range(1, K + 1):
    for y in range(1, N + 1):
        if x - item[y][0] >= 0:  # 현재무게 - 현재물건무게 값이 0이상이라면 (dp테이블에 있다면, 담을 수 있다면)
            dp[x][y] = max(dp[x][y-1], dp[x-item[y][0]][y-1] + item[y][1])  # 왼쪽값, 현재무게-현재물건무게값을 x행으로 한 왼쪽값중 큰 값 선택
        else: # dp테이블에 없다면, 담을 수 없다면
            dp[x][y] = dp[x][y-1]  # 왼쪽 값 선택

print(dp[-1][-1])