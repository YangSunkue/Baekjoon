def solution(n):
    
    def in_cross(row, col, board):
        """
            특정좌표에서 위쪽 대각선 범위 퀸 있는지 확인
        """
        temp_row = row - 1
        temp_col = col - 1
        while 0 <= temp_row < n and 0 <= temp_col < n:
            if board[temp_row][temp_col] == 1:
                return True
            temp_row -= 1
            temp_col -= 1
        
        temp_row = row - 1
        temp_col = col + 1
        while 0 <= temp_row < n and 0 <= temp_col < n:
            if board[temp_row][temp_col] == 1:
                return True
            temp_row -= 1
            temp_col += 1
        
        return False
                
            
    board = [[0 for _ in range(n)] for _ in range(n)]
    visited = [False for _ in range(n)]
    result = 0
    def back_tracking(row):
        
        nonlocal result
        
        if row == n:
            result += 1
            return
        
        for col in range(n):
            if not visited[col] and not in_cross(row, col, board):
                
                visited[col] = True
                board[row][col] = 1
                
                back_tracking(row + 1)
                
                visited[col] = False
                board[row][col] = 0
    
    back_tracking(0)
    return result