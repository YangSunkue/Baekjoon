n = int(input())

a = 0
b = 1
for _ in range(n):
    a, b = b, (a + b)

print(a)