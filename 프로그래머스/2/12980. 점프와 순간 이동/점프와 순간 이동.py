def solution(n):
    
    """
    K 칸 점프: 건전지 K만큼 소모
    총거리 * 2위치 순간이동: 무료
    
    2500 1250 625 312 156 78 39 19 9 4 2 1
    
    2 로 나눠서 나머지가 존재하는 경우 cnt
    n이 0이 되면 종료
    """
    
    result = 0
    while n > 0:
        if n % 2 == 1:
            result += 1
        n //= 2
    return result