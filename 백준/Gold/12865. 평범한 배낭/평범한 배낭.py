import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # 물건의 수, 버틸 수 있는 무게
item = [[]]
for _ in range(N):
    item.append(list(map(int, input().split())))

dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

for x in range(1, K + 1):
    for y in range(1, N + 1):
        if x-item[y][0] >= 0:  # 현재최대무게 - 현재물건무게가 0이상일 경우(dp테이블에 존재할 경우)
            dp[x][y] = max(dp[x][y-1], dp[x-item[y][0]][y-1] + item[y][1])  # [x][y-1], [최대무게-물건무게][y-1] + 물건가치 중 큰 값 선택
        else:  # 현재최대무게 - 현재물건무게가 0미만일 경우(dp테이블에 없을 경우)
            dp[x][y] = dp[x][y-1]  # 좌측 값을 선택

print(dp[-1][-1])
