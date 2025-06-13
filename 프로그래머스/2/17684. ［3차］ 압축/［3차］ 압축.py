def solution(msg):
    
    """인덱스 -> 문자열"""
    index_to_str = ['',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
    
    """문자열 -> 인덱스"""
    str_to_index = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11,
        'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
        'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }
    
    """메인 로직"""
    result = []
    i = 0  # 시작 지점
    
    while i < len(msg):  # 모든 문자를 추출할 때 까지 진행
        
        current = msg[i]
        
        # i 부터 j까지 1칸씩 길게 확장하면서 사전에 있는지 확인
        j = i + 1
        while j <= len(msg) and msg[i:j] in str_to_index:
            current = msg[i:j]
            j += 1
        
        # 가장 긴 문자열 인덱스를 결과에 등록
        result.append(str_to_index[current])
        
        # 다음 문자가 있다면 사전에 등록
        next_index = i + len(current)
        if next_index < len(msg):
            new_string = current + msg[next_index]
            index_to_str.append(new_string)
            str_to_index[new_string] = len(index_to_str) - 1
        
        i = next_index
    
    return result