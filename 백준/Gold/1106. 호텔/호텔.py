import sys
input = sys.stdin.readline

"""
C: C명 확보해야 함
N: 도시 수

cities: [비용, 고객]

1. 1원당 유치고객 수 구해서 역순정렬, 앞부터 도시순회
2. 비용 += (C // 유치고객) * 비용 , (C % 유치고객) 가지고 다음도시로 ㄱ

"""

C, N = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]

# [비용, 고객, 비용 1당 고객수]
for i in range(len(cities)):
    value = cities[i][1] / cities[i][0]  # 비용 1당 고객 수
    cities[i].append(value)
cities.sort(key=lambda x: -x[2])

# dp[i] = i명까지 최소값
dp = [float('inf')] * (C + cities[0][1])
dp[0] = 0

for i in range(1, len(dp)):
    for cost, customer, _ in cities:
        if i >= customer:
            dp[i] = min(dp[i], dp[i - customer] + cost)
        else:
            dp[i] = min(dp[i], cost)

print(min(dp[C:]))