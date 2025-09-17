def solution(N, stages):
    """
    N: 전체 스테이지 개수
    stages: 사용자가 멈춰있는 스테이지 번호 (N + 1은 마지막 스테이지 클리어 한 사용자)
    -> 도전한 사용자 수와 같다

    stages: [2, 1, 2, 6, 2, 4, 3, 3]
    """

    stage_and_fail = [[] for _ in range(N + 1)]  
    for i in range(1, N + 1):
        stage_and_fail[i].append(i)  # [[], [스테이지1], [스테이지2] ...]

    stages.sort()  # [1, 2, 2, 2, 3, 3, 4, 6]
    le = len(stages)
    stages.append(-1)  # [1, 2, 2, 2, 3, 3, 4, 6, -1]

    passed_stg = 0
    stg_and_cnt = [1, 0]

    for i in range(le + 1):
        stage = stg_and_cnt[0]

        if stage != stages[i] and stage <= N:  # 새로운 스테이지 만나면 기존세던거 실패율 계산
            stage_and_fail[stage].append(stg_and_cnt[1] / (le - passed_stg))

            passed_stg += stg_and_cnt[1]
            stg_and_cnt[0] = stages[i]
            stg_and_cnt[1] = 1

            continue

        stg_and_cnt[1] += 1

    result = []
    stage_and_fail.pop(0)  # 빈 리스트 빼기
    for s in stage_and_fail:  # 실패하지 않은 스테이지 실패율 0 추가
        if len(s) == 1:
            s.append(0)

    stage_and_fail.sort(key = lambda x: x[1], reverse=True)
    for re, _ in stage_and_fail:
        result.append(re)
    
    return result