def solution(friends, gifts):
    
    # 선물을 더 많이 준 사람이 받기
    # -> 똑같다면 선물 지수가 높은 사람이 받기
    # -> 선물 지수도 같다면 주지 않기
    
    n = len(friends)
    
    # 이름을 인덱스와 매핑
    name_to_idx = dict()
    for i, name in enumerate(friends):
        name_to_idx[name] = i
    
    # 선물 준 개수 2차원 리스트
    give = [[0] * n for _ in range(n)]
    
    # 총 주고/받은 개수,
    total_give = [0] * n
    total_receive = [0] * n
    
    for gift in gifts:
        
        # 이름 -> 인덱스 변환
        giver, receiver = gift.split()
        g_idx = name_to_idx[giver]
        r_idx = name_to_idx[receiver]
        
        give[g_idx][r_idx] += 1
        total_give[g_idx] += 1
        total_receive[r_idx] += 1
        
    # 선물 지수 계산
    present_score = [0] * n
    for i in range(n):
        present_score[i] = total_give[i] - total_receive[i]
    
    
    next_month = [0] * n
    # 메인 로직
    for i in range(n):
        for j in range(n):
            
            if i == j:
                continue
            
            i_to_j = give[i][j]
            j_to_i = give[j][i]
            
            if i_to_j > j_to_i:
                next_month[i] += 1
            
            elif i_to_j == j_to_i:
                if present_score[i] > present_score[j]:
                    next_month[i] += 1
    
    return max(next_month)