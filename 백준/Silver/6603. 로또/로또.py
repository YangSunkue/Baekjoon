import sys
input = sys.stdin.readline

def back_tracking(depth, start, result):
    
    if depth == 6:
        print(*result)
        return
    
    for i in range(start, len(S)):
        result.append(S[i])
        back_tracking(depth + 1, i + 1, result)
        result.pop()

while True:

    K, *S = map(int, input().split())
    if K == 0: break

    back_tracking(0, 0, [])
    print()