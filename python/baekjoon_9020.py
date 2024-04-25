def is_prime(n): # 소수 판별 함수
    if n == 1:
        False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def binarySearch(list, n, nnum): # 배열, 배열 길이, 찾을 숫자를 인자로 사용
        start = 0
        end = n - 1
        
        while(start <= end):
            mid = (start + end) // 2

            if list[mid] == nnum:
                return True
            elif list[mid] < nnum:
                start = mid + 1
            else:
                end = mid - 1

        return False

cnt = 2
prime_list = []

for _ in range(int(input())):
    num = int(input())
    partition = []
    
    for i in range(cnt, num + 1): # 소수 리스트 구하기
        if is_prime(i):
            prime_list.append(i)
            
        cnt = num # 이미 구했던 소수를 제외하기 위한 키값
    

    for p in prime_list:
        if (num // 2 + 1) < p: # 불필요한 연산을 없애기 위해 num 중간값까지만 계산한다
            break

        # num - p가 소수일 경우, 골드바흐 파티션이다
        # p값을 큰 값부터 작은 값 순으로 사용하면, 파티션 1개를 찾고 바로 탈출할 수 있다.(아직구현안함)
        if binarySearch(prime_list, len(prime_list), num - p):
            partition.append([p, num - p])
            partition[-1].sort()

        
    # 파티션이 여러개일 수 있으므로 , 두 수의 차이가 가장 적은 값 출력( 마지막에 추가된 값 )
    print(partition[-1][0], partition[-1][1])

