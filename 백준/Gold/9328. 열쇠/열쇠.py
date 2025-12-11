from collections import deque, defaultdict
import sys
input = sys.stdin.readline
"""
소문자: 열쇠
대문자: 문

.   : 빈 공간
*   : 벽
$   : 문서
"""
def can_go(nx, ny):
    return 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and board[nx][ny] != '*'

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(int(input())):

    h, w = map(int, input().split())                    # 높이, 너비
    board = [list(input().strip()) for _ in range(h)]   # 맵
    keys = set()                                        # 키
    for key in input().strip():
        if key == '0':
            continue
        keys.add(key.upper())

    """
    모든 시작점 큐에 넣고 단일 BFS
    새 열쇠 획득 시, 해당하는 문들 큐에 추가
    큐에 넣을 때 visited 체크
    """
    visited = [[False] * w for _ in range(h)]
    doors = defaultdict(list)  # {'A': [(2, 3), (6, 4), ...]}

    result = 0
    queue = deque([])

    # 모든 시작점을 큐에 넣고 시작
    for x in range(h):
        for y in range(w):
            if (x == 0 or x == h-1 or y == 0 or y == w-1) and can_go(x, y):
                queue.append((x, y))
                visited[x][y] = True
    
    while queue:

        cx, cy = queue.popleft()
        item = board[cx][cy]

        # 문
        if item.isupper():
            if item not in keys:
                visited[cx][cy] = False
                doors[item].append((cx, cy))
                continue
        
        # 문서
        if item == '$':
            result += 1

        # 열쇠
        if item.islower():
            new_key = item.upper()
            if new_key not in keys:
                keys.add(new_key)

                for i, j in doors[new_key]:
                    queue.append((i, j))
                    visited[i][j] = True
                doors[new_key] = []
        
        # 다음 좌표 탐색
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if can_go(nx, ny):
                queue.append((nx, ny))
                visited[nx][ny] = True
    
    print(result)