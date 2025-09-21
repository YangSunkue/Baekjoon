import math

def solution(progresses, speeds):

    """
    progresses: 작업별 진행도 [93, 30, 55]
    speeds: 작업별 진행속도 [1, 30, 5]

    배포가능일을 미리 계산해두기
    """

    le = len(progresses)

    # 배포 가능일
    deploy_day = [0 for _ in range(le)]
    for i in range(le):
        deploy_day[i] = math.ceil(((100 - progresses[i]) / speeds[i]))
    
    result = []
    count = 0
    point_day = deploy_day[0]
    for i in range(le):
        if point_day >= deploy_day[i]:
            count += 1
        else:
            result.append(count)
            point_day = deploy_day[i]
            count = 1
    result.append(count)
    
    return result