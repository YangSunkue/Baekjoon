from collections import deque

n, k = map(int, input().split())
result = []

human = deque()
for i in range(n): # 1 ~ n을 queue에 담는다
    human.append(i + 1)

while human:  # 사람이 다 죽으면 반복 종료
    for _ in range(k - 1):
        human.append(human.popleft()) # k번째 사람을 죽여야 하니, k - 1번 이동하여 죽일 사람 선택
    result.append(str(human.popleft())) # 선택된 사람 죽여서 결과 리스트에 순서대로 담기

print('<', end='')
print(', '.join(result), end='')
print('>')