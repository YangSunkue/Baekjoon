a = int(input())
llist = list(map(int, input().split()))

def is_prime(n):
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