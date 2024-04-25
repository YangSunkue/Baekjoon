x = int(input())

d = [0] * (x + 2)
d[1] = 1
d[2] = 2

for i in range(3, x + 1):
    d[i] = (d[i-1] + d[i-2]) % 15746

print(d[x])




# 1 2 3 4 5  6   7
# 1 2 3 5 8 13 21