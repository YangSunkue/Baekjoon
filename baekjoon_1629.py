def dac(a, b, c): # a^b % c
    if b == 1:
        return a % c
    elif b % 2 == 0: # b가 짝수일 때
        return (dac(a, b//2, c)**2) % c
    else:
        return ((dac(a, b//2, c)**2)*a) % c

a, b, c = map(int, input().split())
print(dac(a, b, c))