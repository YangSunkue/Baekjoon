def solution(rows, columns, queries):
    
    """
    직사각형을 시계방향으로 회전시키고 최솟값을 리턴한다.
    """
    def rotate(x1, y1, x2, y2):

        min_value = int(1e9)
        move_x = x2 - x1
        move_y = y2 - y1
        origin_value = table[x1][y1]  # 첫번째 좌표 값
        
        cur_x = x1
        cur_y = y1
        # 하, 우, 상, 좌로 움직이며 돌리기
        for _ in range(move_x):
            cur_x += 1
            value = table[cur_x][cur_y]
            table[cur_x - 1][cur_y] = value
            min_value = min(min_value, value)
            
        for i in range(move_y):
            cur_y += 1
            value = table[cur_x][cur_y]
            table[cur_x][cur_y - 1] = value
            min_value = min(min_value, value)
        
        for i in range(move_x):
            cur_x -= 1
            value = table[cur_x][cur_y]
            table[cur_x + 1][cur_y] = value
            min_value = min(min_value, value)
        
        for i in range(move_y - 1):
            cur_y -= 1
            value = table[cur_x][cur_y]
            table[cur_x][cur_y + 1] =  value
            min_value = min(min_value, value)
        
        table[x1][y1 + 1] = origin_value
        
        return min(min_value, origin_value)
            
            
    """테이블 생성"""
    table = [[] for _ in range(rows)]
    
    num = 0
    for i in range(rows):
        for j in range(columns):
            num += 1
            table[i].append(num)
    
    """메인 로직"""
    result = []
    for q in queries:
        x1, y1, x2, y2 = q
        result.append(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1))
    
    """결과 출력"""
    return result