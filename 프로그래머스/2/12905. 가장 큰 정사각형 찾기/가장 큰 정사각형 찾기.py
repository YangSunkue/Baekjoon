def solution(board):
    
    x = len(board)
    y = len(board[0])
    
    if x == 1:
        return max(board[0])
    
    dp = []
    dp.append([0] * (y + 1))
    for i in range(x):
        dp.append([0] + board[i])
    
    result = 0
    for i in range(2, x + 1):
        for j in range(1, y + 1):
            
            if dp[i][j] == 0:
                continue
            
            diagonal = dp[i - 1][j - 1]
            left = dp[i][j - 1]
            up = dp[i - 1][j]
            
            value = min(diagonal, left, up) + 1
            dp[i][j] = value
            
            if value > result:
                result = value
    
    return result * result