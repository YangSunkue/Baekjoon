def solution(arr1, arr2):
    
    # 행, 열 크기 구하기
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    # 결과 담을 빈 행렬 만들기
    result = [[0] * c2 for _ in range(r1)]

    # 행렬의 곱 계산
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result