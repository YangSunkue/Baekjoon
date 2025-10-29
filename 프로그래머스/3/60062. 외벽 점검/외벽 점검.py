from itertools import permutations

def solution(n, weak, dist):

    le = len(weak)

    # 인덱스 오류 방지를 위한 확장
    for i in range(le):
        weak.append(weak[i] + n)

    result = len(dist) + 1

    # 모든 취약점을 시작점으로
    for i in range(le):

        # 모든 시작점에 대해, 모든 경우의 수 탐색
        for friend in permutations(dist, len(dist)):
            cnt = 1
            position = weak[i] + friend[cnt - 1]

            # 필요한 사람 수 계산
            for j in range(i, i + le):
                if position < weak[j]:
                    cnt += 1

                    if cnt > len(dist):
                        break

                    position = weak[j] + friend[cnt - 1]
            else:
                result = min(result, cnt)
    
    return result if result <= len(dist) else -1