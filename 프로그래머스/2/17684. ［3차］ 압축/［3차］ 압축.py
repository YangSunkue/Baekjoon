def solution(msg):
    
    """인덱스 -> 문자열"""
    index_to_str = [''] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    
    """문자열 -> 인덱스"""
    str_to_index = dict()
    for i in range(26):
        char = chr(ord('A') + i)
        str_to_index[char] = i + 1
    
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
            str_to_index[new_string] = len(index_to_str)
            index_to_str.append(new_string)
            
        i = next_index
    
    return result