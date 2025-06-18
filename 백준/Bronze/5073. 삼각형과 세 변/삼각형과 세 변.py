import sys
input = sys.stdin.readline

while True:
    t = list(map(int, input().split()))
    t.sort(reverse=True)
    
    if t.count(0) == 3:
        break

    if t[0] >= sum(t[1:]):
        print('Invalid')
    elif t[0] == t[1] and t[1] == t[2]:
        print('Equilateral')
    elif t[0] == t[1] or t[0] == t[2] or t[1] == t[2]:
        print('Isosceles')
    else:
        print('Scalene')
