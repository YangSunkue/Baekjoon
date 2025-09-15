def solution(n):
    
    """
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    go(진행 칸 수): N, N-1, N-2, N-3, N-4 ... (go >= 1)
    -> 1칸씩 줄이며 진행하다 종료
    
    하: x += 1
    우: y += 1
    상: x -= 1, y -= 1
    """
    
    tri = [[0 for _ in range(i)] for i in range(1, n + 1)]
    directions = [(1, 0), (0, 1), (-1, -1)]
    try_count = [i for i in range(n, 0, -1)]

    dx, dy = -1, 0
    num = 1
    try_idx = 0
    should_break = False
    while num <= 550000:
        
        # 하, 우, 상
        for i in range(3):
            
            for _ in range(try_count[try_idx]):
                dx = dx + directions[i][0]
                dy = dy + directions[i][1]
                
                tri[dx][dy] = num
                
                num += 1
            
            try_idx += 1
            if try_idx >= n:
                should_break = True
                break
        if should_break:
            break
    
    result = []
    for tr in tri:
        for t in tr:
            result.append(t)
    
    return result