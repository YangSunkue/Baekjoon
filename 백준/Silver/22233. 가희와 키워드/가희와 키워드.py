import sys
input = sys.stdin.readline

N, M = map(int, input().split())
note = set()
for _ in range(N):
    note.add(input().strip())

for _ in range(M):
    words = list(input().strip().split(','))
    
    for word in words:
        note.discard(word)
    
    print(len(note))