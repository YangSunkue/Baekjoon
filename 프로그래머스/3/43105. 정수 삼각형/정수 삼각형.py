def solution(triangle):
    
    """
    [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5]
    ]
    """
    
    le = len(triangle)
    
    dp = [[0] * le for _ in range(le)]
    for i in range(le):
        dp[-1][i] = triangle[-1][i]
    
    for i in range(le - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
    
    return dp[0][0]