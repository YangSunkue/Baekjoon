import sys
input = sys.stdin.readline

S = set()
for _ in range(int(input())):

    cmd = list(input().split())
    if cmd[0] == 'add':
        S.add(cmd[1])
    
    elif cmd[0] == 'remove':
        S.discard(cmd[1])
    
    elif cmd[0] == 'toggle':
        if cmd[1] in S:
            S.remove(cmd[1])
        else:
            S.add(cmd[1])
    
    elif cmd[0] == 'all':
        S = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'}
    
    elif cmd[0] == 'empty':
        S.clear()
    
    elif cmd[0] == 'check':
        if cmd[1] in S:
            print(1)
        else:
            print(0)

