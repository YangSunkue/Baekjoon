import sys
input = sys.stdin.readline

"""
k개의 문제를 풀면 0점 ~ 100점 획득함 -> 팀ID/문제번호/점수 저장
한 문제를 여러 번 제출하면, 최고점수가 최종점수 -> 제출안하면 0점
팀의 점수는 각 문제 최종 점수의 합

점수가 동일한 팀이 있을 경우
1. 점수가 같으면, 제출 횟수가 적은 팀이 이긴다
2. 점수와 제출 횟수가 같으면, 마지막 제출 시간이 빠른 팀이 이긴다

점수 높은순, 제출횟수 적은순, 제출시간 빠른순
"""
for _ in range(int(input())):

    """
    n: 팀 개수 (3 <= n)
    k: 문제 개수 (k <= 100)
    team: 나의 팀 (1 <= t <= n)
    m: 로그 개수 (3 <= m <= 10000)
    """
    n, k, my_team, m = map(int, input().split())

    # [[문제1점수, 문제2점수, ... 크기는 k + 1] 이걸 n + 1개수만큼 팀별로 할당]
    team_and_score = [[0] * (k + 1) for _ in range(n + 1)]  # 1 based

    # 정렬용 리스트 -> 팀별 총합점수, 제출횟수, 마지막 제출시간
    score_count_time = [[0, 0, int(1e9)] for _ in range(n + 1)]  # 1 based

    """로그 입력받기"""
    for submit in range(m):
        """
        cur_team: 팀 id
        num: 문제 번호
        score: 획득한 점수
        """
        cur_team, num, score = map(int, input().split())
        # print(f'cur_team, 문제번호, 점수: {cur_team}, {num}, {score}')

        # 각 문제는 더 높은 점수로 갱신
        team_and_score[cur_team][num] = max(team_and_score[cur_team][num], score)
        # 제출횟수 더하기
        score_count_time[cur_team][1] += 1
        # 마지막 제출시간 갱신
        score_count_time[cur_team][2] = submit
    
    """계산된 팀별 점수를 정렬용 리스트에 할당"""
    for team in range(1, n + 1):
        score_count_time[team][0] = sum(team_and_score[team])
        score_count_time[team].append(team)  # 정렬되면 인덱스로 구분되던 팀이 섞이니, 팀 번호를 리스트에 추가해준다
    
    """문제 조건대로 정렬"""
    score_count_time.sort(key = lambda x: (-x[0], x[1], x[2]))
    # print(f'오니? 정렬된리스트: {score_count_time}')

    for rank in range(len(score_count_time) - 1):
        # 우리 팀 랭킹 출력
        if score_count_time[rank][-1] == my_team:
            print(rank + 1)
            break

# 1
# 3 4 3 5
# 1 1 30
# 2 3 30
# 1 2 40
# 1 2 20
# 3 1 70