a = int(input())
llist = list(map(int, input().split()))

def is_prime(n): # 소수 판별 함수
    if n == 1:
        False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

result = 0
for i in llist:
    if i == 1:
        continue
    if is_prime(i):
        result += 1
        
print(result)