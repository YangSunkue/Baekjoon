def solution(n, m, x, y, r, c, k):

    def get_manhatten(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    def can_go(x, y):
        return 0 <= x < n and 0 <= y < m
    
    x, y, r, c = x - 1, y - 1, r - 1, c - 1
    directions = {'d': (1, 0), 'l': (0, -1), 'r': (0, 1), 'u': (-1, 0)}

    distance = get_manhatten(x, y, r, c)
    if distance > k or (k - distance) % 2 == 1:
        return 'impossible'
    
    step = 0
    result = ''
    while step < k:

        for direction, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy

            if not can_go(nx, ny):
                continue

            distance = get_manhatten(nx, ny, r, c)
            if distance > k - (step + 1) or (k - (step + 1) - distance) % 2 == 1:
                continue
            
            x, y = nx, ny
            step += 1
            result += direction
            break

        else:
            return 'impossible'
    
    return result