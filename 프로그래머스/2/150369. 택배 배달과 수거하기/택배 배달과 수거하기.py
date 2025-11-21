def solution(cap, n, deliveries, pickups):
    
    """
    그리디하게 먼곳부터 배달 및 수거
    몇 개 가져가느냐는 생각할 필요 없음
    어디부터 주냐도 생각할 필요 없음
    
    -> 가장 먼 곳부터 가되 배달, 수거 무조건 cap개씩 줄이면 됨
    """
    
    deliver = 0
    pickup = 0
    result = 0
    
    for i in range(n - 1, -1, -1):
        deliver += deliveries[i]
        pickup += pickups[i]
        
        while deliver > 0 or pickup > 0:
            deliver -= cap
            pickup -= cap
            result += (i + 1) * 2
    
    return result