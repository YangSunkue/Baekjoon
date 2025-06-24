from collections import defaultdict
import sys
input = sys.stdin.readline

"""
한 팀: 6명, 6명 미만 팀 제외
팀 점수: 상위 4명 점수 합산
-> 결승선을 통과한 순서대로 점수 부여
-> 가장 낮은 점수 얻은 팀이 우승
-> 동점일 경우 다섯번째 주자가 빨리 들어온 팀이 우승

N: 총 선수 숫자
players: 선수들이 들어온 순서
"""

"""테스트 케이스 개수만큼 반복"""
for _ in range(int(input())):

    """
    0. dict에 존재하는 팀만이 6명 이상의 팀

    1. players 집합화 중복 제거
    2. 모든 팀에 대해 players.count로 6명 이상인지 셈.
    3. 1 based 리스트로 각 팀이 6명 이상인지 아닌지를 True/False로 저장
    4. players를 반복하면서 True일 경우 딕셔너리 list에 값 추가
    """
    
    # 팀별 점수 리스트를 매핑
    teams = defaultdict(list)

    N = int(input())
    players = list(map(int, input().split()))

    can_win = [False for _ in range(N + 1)]
    players_set = set(players)

    # 각 팀이 몇 명인지 세고, 6명 이상이면 can win 설정
    for player in players_set:
        if players.count(player) >= 6:
            can_win[player] = True
    
    # 6명 이상인 팀에만 점수 부여
    score = 1
    for player in players:
        if can_win[player]:
            teams[str(player)].append(score)
            score += 1

    # 6명 이상인 팀들 중 1등 정하기
    winner = (0, int(1e9), int(1e9))  # 팀번호, 합산점수, 5번째 주자 점수 -> 낮아야 우승함
    for team in teams:
        if len(teams[team]) >= 6:

            # 팁 합산 점수
            team_score = sum(teams[team][:4])
            # 다섯번째 주자 점수
            five_score = teams[team][4]

            # 기존 우승후보 팀보다 점수가 낮을 경우 우승후보 팀 교체
            if team_score < winner[1]:
                winner = (team, team_score, five_score)

            # 기존 우승후보 팀과 점수가 같으면 5번째 주자 점수로 결정
            elif team_score == winner[1]:
                if five_score < winner[2]:
                    winner = (team, team_score, five_score)
    
    print(winner[0])
