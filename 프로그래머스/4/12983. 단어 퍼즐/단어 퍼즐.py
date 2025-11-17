def solution(strs, t):
    
    """
    dp[i]: 0~i 까지 필요한 단어 수
    """
    
    n = len(t)

    dp = [float('inf') for _ in range(n + 1)]
    dp[0] = 0
    
    strs = set(strs)
    sizes = set(len(s) for s in strs)
    
    for i in range(1, n + 1):
        for size in sizes:
            if (i - size) >= 0 and t[i - size : i] in strs:
                dp[i] = min(dp[i], dp[i - size] + 1)
    
    return dp[-1] if dp[-1] != float('inf') else -1