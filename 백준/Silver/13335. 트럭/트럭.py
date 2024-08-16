from collections import deque
import sys
input = sys.stdin.readline

N, W, L = map(int, input().split())
truck = list(map(int, input().split()))

q = deque([0] * W) # 큐 사용
time = 0 # 경과시간
while q:
    time += 1 # 반복할 때마다 시간 증가
    q.popleft()

    if truck:
        if sum(q) + truck[0] <= L: # 무게 제한에 걸리지 않으면 다리에 올리기
            q.append(truck.pop(0))
        else:
            q.append(0) # 무게에 걸렸다면, 다리길이를 맞추기 위해 0 추가

print(time)