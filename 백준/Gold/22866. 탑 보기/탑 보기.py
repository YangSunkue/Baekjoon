"""
골드 3
스택

오른쪽으로 한번, 왼쪽으로 한번 순회
"""
N = int(input())
b = list(map(int, input().split()))

left_buildings = [[0] * 2 for _ in range(N)]  # [[건물개수, 가까운왼쪽건물], [건물개수, 가까운왼쪽건물] ...]
right_buildings = [[0] * 2 for _ in range(N)]

# 좌측에 보이는 건물 탐색
stack = []
for idx in range(N):
    while stack and b[stack[-1]] <= b[idx]:
        stack.pop()
    
    if stack:
        left_buildings[idx][0] = len(stack)
        left_buildings[idx][1] = stack[-1] + 1

    stack.append(idx)

# 우측에 보이는 건물 탐색
stack = []
for idx in range(N - 1, -1, -1):
    while stack and b[stack[-1]] <= b[idx]:
        stack.pop()
    
    if stack:
        right_buildings[idx][0] = len(stack)
        right_buildings[idx][1] = stack[-1] + 1

    stack.append(idx)

# 결과 종합
result = [[0] * 2 for _ in range(N)]
for i in range(N):

    result[i][0] = left_buildings[i][0] + right_buildings[i][0]

    l = left_buildings[i][1]
    r = right_buildings[i][1]
    if l > 0 and r > 0:
        l_dist = abs((i + 1) - l)
        r_dist = abs((i + 1) - r)

        if l_dist < r_dist:
            result[i][1] = l
        elif l_dist > r_dist:
            result[i][1] = r
        else:
            result[i][1] = min(l, r)



    elif l == 0 or r == 0:
        result[i][1] = max(l, r)
    elif l == 0 and r == 0:
        result[i][1] = 0

for r in result:
    print(0) if r[0] == 0 else print(*r)