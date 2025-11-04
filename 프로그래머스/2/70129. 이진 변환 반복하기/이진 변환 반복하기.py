def solution(s):
    
    """
        1. 0을 제거
        2. 길이 측정
        3. 길이를 2진법으로 변환
    """
    
    def to_binary(num):
        """입력받은 숫자를 2진법 문자열로 반환한다."""
        num = int(num)
        result = []
        while True:
            result.append(num % 2)            
            if num <= 1:
                break
            num //= 2
        
        result.reverse()
        return ''.join(map(str, result))
    
    changed_cnt = 0  # 변환횟수
    deleted_zero = 0  # 제거된 0 개수
    while s != '1':
        
        print(s)
        
        deleted = s.count('0')
        s = to_binary(len(s) - deleted)
        
        deleted_zero += deleted
        changed_cnt += 1
    
    return [changed_cnt, deleted_zero]










