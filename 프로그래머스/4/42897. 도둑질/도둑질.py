def solution(money):
    
    le = len(money)
    
    dp1 = [0 for _ in range(le + 2)]
    dp2 = [0 for _ in range(le + 2)]
    
    # 첫번째 집 포함
    for i in range(2, le + 1):
        dp1[i] = max(dp1[i - 2] + money[i - 2], dp1[i - 1])
    
    # 첫번째 집 미포함
    for i in range(3, le + 2):
        dp2[i] = max(dp2[i - 2] + money[i - 2], dp2[i - 1])
    
    return max(dp1[-2], dp2[-1])