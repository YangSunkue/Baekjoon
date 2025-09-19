def solution(b, moves):

    n = len(b)

    bucket = []
    result = 0

    board = [[] for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n):
            item = b[i][j]

            if item != 0:
                board[j].append(b[i][j])

    for m in moves:
        if board[m - 1]:
            item = board[m - 1].pop()
            
            if bucket and item == bucket[-1]:
                bucket.pop()
                result += 2
            
            else:
                bucket.append(item)
    
    return result