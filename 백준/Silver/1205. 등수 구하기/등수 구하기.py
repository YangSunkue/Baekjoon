import sys
input = sys.stdin.readline

"""
N: 현재 랭킹 등록된 점수 개수
new_score: 태수의 새로운 점수
P: 랭킹 리스트에 올라갈 수 있는 점수 개수

태수의 점수는 몇등인지 출력, 랭킹에 못들어가면 -1 출력
"""
N, new_score, P = map(int, input().split())

"""기존 랭킹이 존재할 경우 메인 로직 진행"""
if N > 0:

    r = list(map(int, input().split()))  # 크기: N

    """각 점수에 정확한 순위 부여"""
    ranks = [[score] for score in r]

    # 태수의 점수 추가하고 정렬
    ranks.append([new_score])
    ranks.sort(reverse=True)
    ranks[0].append(1)  # 가장 앞에 있는 요소는 1등

    prev = ranks[0]  # 점수와 순위 ex) [100, 1]
    for i in range(1, len(ranks)):

        # 윗 순위와 점수가 같으면 같은 순위 부여
        if prev[0] == ranks[i][0]:
            ranks[i].append(prev[1])

        # 점수가 낮으면 다음 순위 부여
        else:
            ranks[i].append(i + 1)
            prev = ranks[i]
    

    """태수의 순위 출력"""
    for i in range(len(ranks) - 1, -1, -1):

        # 태수의 점수
        if ranks[i][0] == new_score:

            # 랭킹 안에 들었다면 순위 출력
            if i < P :
                print(ranks[i][1])
                
            # 랭킹에 못 들었다면 -1 출력
            else:
                print(-1)
            break

# 현재 랭킹이 없다면 무조건 1등이다
else:
    print(1)