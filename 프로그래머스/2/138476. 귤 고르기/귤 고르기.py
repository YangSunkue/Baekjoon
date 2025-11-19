from collections import defaultdict

def solution(k, tangerines):
    
    """
    [1, 2, 2, 3, 3, 4, 5, 5]
    
    1. 크기별 개수 세기
    2. k가 될 때까지, 개수가 가장 많은 귤 넣기
    3. len(set(t)) 구하기
    """
    
    size_to_num = defaultdict(int)
    
    for tangerine in tangerines:
        size_to_num[tangerine] += 1
    size_to_num = defaultdict(int, sorted(size_to_num.items(), key=lambda x: -x[1]))
    
    t = set()
    count = 0
    for size in size_to_num:
        
        t.add(size)
        
        if count + size_to_num[size] < k:
            count += size_to_num[size]
            
            continue
        else:
            break
    
    return len(t)