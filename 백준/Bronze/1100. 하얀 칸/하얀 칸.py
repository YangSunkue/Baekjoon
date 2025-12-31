board = [list(input().strip()) for _ in range(8)]

result = 0
for x in range(8):
    for y in range(8):
        if ((x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1)) and board[x][y] == 'F':
            result += 1

print(result)