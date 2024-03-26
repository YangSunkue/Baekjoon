from collections import deque

n, k = map(int, input().split())
human = deque()
result = []

for i in range(n): # 사람 목록
    human.append(i+1)

while human: # 사람이 다 죽으면 반복 종료
    for i in range(k-1): # k번째 사람을 죽여야 하니 k-1번 이동후 죽이기
        human.append(human.popleft())
    result.append(str(human.popleft())) # join 쓰려면 문자열이어야 함

print('<', end='')
print(', '.join(result), end='')
print('>')