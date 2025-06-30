import sys
input = sys.stdin.readline

"""
N: 식탁의 길이
K: K 이하 거리 햄버거 먹기 가능
table: 사람과 햄버거의 위치

사람 기준 순서대로 왼쪽이든 오른쪽이든 가장 가까운거 먹으면 될거같은데..? 그리디?
K가 최대 10이니 가능할거같다. K <= N이었으면 힘들었을듯.

1. table 1회 순회
2. visited를 사용한다.
3. 방문하지 않았다면 기준을 방문 처리하고 진행한다 -> 햄버거일 경우 K내의 사람을 찾고, 사람일 경우 K내의 햄버거를 찾는다.
4. 찾았으면 찾은 애도 방문 처리하고 result를 1 증가시킨다. 찾지 못했으면 그냥 넘어간다.
"""

def can_eat(idx, K):

    # 기준 (사람 또는 햄버거)
    point = table[idx]
    # idx 뒤로 K거리만큼 잘라낸다 (슬라이싱은 인덱스오류 안남)
    sliced_table = table[idx + 1: idx + K + 1]

    # 거리 내에 있는 햄버거/사람을 찾으면 방문 처리
    for i in range(len(sliced_table)):
        if point != sliced_table[i] and not visited[idx + 1 + i]:
            visited[idx + 1 + i] = True
            return True
            
    return False
            
N, K = map(int, input().split())
table = list(input().strip())
visited = [False] * N

result = 0
for i in range(N):

    # 아직 매칭되지 않은 사람/햄버거에 대해 진행
    if not visited[i]:
        visited[i] = True

        if can_eat(i, K):
            result += 1

print(result)