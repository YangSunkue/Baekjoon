from itertools import permutations

def solution(n, weak, dist):
    """
    n: 외벽 범위
    weak: 취약점 위치 리스트
    dist: 친구별 이동 거리 리스트
    
    1. dist를 가지고 모든 permutations (경우의 수 순열)을 계산한다.
    2. 이동거리를 더해가며 다음 취약점들을 커버할 수 있는지 순차적으로 검사하며,
        커버 불가능 할 경우 친구 수를 늘려 해당 친구 위치부터 탐색한다.
    3. weak 모든 요소를 시작점으로 삼아 반복한다.
    """
    
    le = len(weak)
    
    # 인덱싱 오류 방지를 위해 2배로 늘린다
    for i in range(n):
        weak.append(weak[i] + n)
    
    
    # 모든 취약점을 시작점으로
    result = len(dist) + 1
    for i in range(le):
        
        # 각 시작점에 대해 모든 경우의 수 대입 탐색
        for friend in permutations(dist, len(dist)):
            
            cnt = 1
            position = weak[i] + friend[cnt - 1]
            for j in range(i, i + le):
                if position < weak[j]:
                    cnt += 1
                    
                    if cnt > len(dist):
                        break
                    
                    position = weak[j] + friend[cnt - 1]
            else:
                result = min(result, cnt)
    
    return result if result <= len(dist) else -1