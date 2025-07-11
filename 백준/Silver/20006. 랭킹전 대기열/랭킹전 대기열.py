import sys
input = sys.stdin.readline

"""
players: 플레이어 수
limit: 방의 정원

방에는 처음 입장한 플레이어 기준 -10 ~ +10 까지 입장 가능
-> if 절댓값(방장레벨 - 플레이어레벨) <= 10:

1. 입장 가능한 방 없을 경우, 새로운 방 생성
2. 방에 들어간 후 정원이 찰 때까지 대기
3. 입장 가능한 방이 여러개일 경우 "먼저 생성된" 방 입장

방 생성된 순서대로 출력
꽉 찬 방은 Started! + 레벨, 닉네임 출력 -> 닉네임 오름차순
덜 찬 방은 Waiting! + 레벨, 닉네임 출력 -> 닉네임 오름차순
[레벨, 닉네임], [레벨, 닉네임]

rooms = [
        [(10, a), (15, b)], 0번 방
        [], 1번 방
        ...
        ]
"""

players, limit = map(int, input().split())

"""방에 입장시키기"""
rooms = []
for i in range(players):

    values = list(input().strip().split())
    level, name = int(values[0]), values[1]

    """들어갈 방이 있는지 확인"""
    for room in rooms:
        if len(room) < limit and abs(room[0][0] - level) <= 10:
            room.append((level, name))
            break
    else:
        # 들어갈 방이 없는 경우 방 생성
        rooms.append([(level, name)])

"""결과 출력"""
for room in rooms:

    # 방 인원수에 따라 시작/대기 출력
    if len(room) >= limit:
        print('Started!')
    else:
        print('Waiting!')
    
    # 닉네임 오름차순 정렬
    room.sort(key = lambda x: x[1])
    for player in room:
        print(*player)
