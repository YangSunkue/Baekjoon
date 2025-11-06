def solution(keyinput, board):
    
    directions = {'up': (0, 1), 'down': (0, -1), 'left': (-1, 0), 'right': (1, 0)}
    
    width = board[0] // 2
    height = board[1] // 2
    
    def can_go(ny, nx):
        return -width <= ny <= width and -height <= nx <= height
    
    cx, cy = (0, 0)
    for key in keyinput:
        dx, dy = directions[key]
        nx, ny = cx + dx, cy + dy
        
        if can_go(nx, ny):
            cx, cy = nx, ny
    
    return [cx, cy]