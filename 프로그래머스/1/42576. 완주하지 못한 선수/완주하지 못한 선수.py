from collections import defaultdict

def solution(part, comp):
    
    """
    part: 참여한 선수들
    comp: 완주한 선수들
    
    완주하지 못한 선수 출력 (딱 한명)
    """
    
    # 완주자 딕셔너리 {완주자명: 수}
    comp_dict = defaultdict(int)
    for name in comp:
        comp_dict[name] += 1
    
    for name in part:
        if comp_dict[name] == 0:
            return name
        
        comp_dict[name] -= 1