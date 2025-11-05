def solution(brown, yellow):
    
    total = brown + yellow
    
    # 세로 길이를 3부터 1씩 증가시킨다
    for height in range(3, total):
        
        # 사각형이 가능할 경우
        if total % height == 0:
            width = total // height
            
            # 카펫 개수가 맞는 경우
            if (height + width) * 2 - 4 == brown:
                return [width, height]