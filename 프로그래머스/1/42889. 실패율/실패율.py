def solution(N, stages):
    
    # 스테이지별 실패자 수
    # 인덱스와 맞추기 위함(+1) + 전부 클리어한 사람 저장하기 위함(+1)
    failures = [0] * (N + 2)
    for stage in stages:
        failures[stage] += 1
    
    # 스테이지별 실패율
    fails = dict()
    total = len(stages)
    
    # 실패율 구하기
    for i in range(1, N + 1):
        
        # 실패자가 한명도 없으면 해당 스테이지 실패율 0
        if failures[i] == 0:
            fails[i] = 0
            continue
        
        # 실패율: 해당 스테이지 실패자 / 도전자
        fails[i] = failures[i] / total
        total -= failures[i]
    
    result = sorted(fails, key = lambda x: fails[x], reverse = True)
    
    return result