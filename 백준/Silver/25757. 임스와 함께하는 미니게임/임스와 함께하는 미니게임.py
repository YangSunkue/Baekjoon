import sys
input = sys.stdin.readline

"""
N: 플레이 신청 횟수
game: 게임 종류
    Y: 윷놀이, 2명
    F: 같은 그림 찾기, 3명
    O: 원카드, 4명
"""
N, game = input().split()
N = int(N)

gamers = set()
for _ in range(N):
    gamers.add(input().strip())

if game == 'Y':
    print(len(gamers))
elif game == 'F':
    print(len(gamers) // 2)
elif game == 'O':
    print(len(gamers) // 3)