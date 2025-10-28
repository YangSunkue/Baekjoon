def solution(k, dungeons):
    
    """
        k: 현재 피로도
        dungeons: [최소피로도, 소모피로도]
        
        최대 탐험 가능 던전 수 리턴
        
        len(dungeons) 만큼 뽑는 순열 구해서 완전탐색
    """
    
    n = len(dungeons)
    
    visited = [False for _ in range(n)]
    result = 0
    def back_tracking(tired, cnt):  # 피로도, 탐험 던전 수
        
        nonlocal result
        result = max(result, cnt)
        
        for i in range(n):
            min_t = dungeons[i][0]
            use_t = dungeons[i][1]
            
            if tired >= min_t and not visited[i]:
                visited[i] = True
                back_tracking(tired - use_t, cnt + 1)
                visited[i] = False
    
    back_tracking(k, 0)
    return result