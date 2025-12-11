from collections import deque, defaultdict
import sys
input = sys.stdin.readline
def can_go(nx, ny):
    return 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and board[nx][ny] != '*'
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(int(input())):

    h, w = map(int, input().split())
    board = [list(input().strip()) for _ in range(h)]
    keys = set()
    for key in input().strip():
        keys.add(key.upper())
    
    result = 0
    visited = [[False] * w for _ in range(h)]
    queue = deque([])
    doors = defaultdict(list)

    # 모든 시작점 큐에 넣기
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
                doors[item].append((cx, cy))
                visited[cx][cy] = False
                continue
        
        # 열쇠
        if item.islower():
            new_key = item.upper()
            if new_key not in keys:
                keys.add(new_key)

                for i, j in doors[new_key]:
                    queue.append((i, j))
                    visited[i][j] = True
                    doors[new_key] = []
        
        # 문서
        if item == '$':
            result += 1
        
        # 4방향 큐에 추가
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if can_go(nx, ny):
                queue.append((nx, ny))
                visited[nx][ny] = True
    
    print(result)