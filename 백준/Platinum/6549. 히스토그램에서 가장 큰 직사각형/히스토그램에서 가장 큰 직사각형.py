import sys
input = sys.stdin.readline

while True:
    data = list(map(int, input().split()))
    n = data[0]
    squares = data[1:]

    if n == 0:
        break

    stack = []
    max_size = 0
    squares.append(0)

    for i, h in enumerate(squares):
        while stack and squares[stack[-1]] > h:
            height = squares[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_size = max(max_size, height * width)
        stack.append(i)
    
    print(max_size)