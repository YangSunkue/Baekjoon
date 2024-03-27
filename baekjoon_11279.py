import heapq as hq
import sys

n = int(input())
hqq = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x >= 1:
        hq.heappush(hqq, -x)  # hq는 최소힙만 지원하기 때문에, 최대힙 처럼 사용하기 위해 음수로 저장
    else:                   # 음수로 저장하면 -가 붙으니, 가장 큰 값이 가장 위로 가게 된다
        if len(hqq) == 0:
            print(0)
        else:
            print(abs(hq.heappop(hqq)))  # 값을 꺼낼 땐 절댓값을 이용해 양수로 만든다