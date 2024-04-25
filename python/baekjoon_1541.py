string = input().split('-')

result = 0

for i in string[0].split('+'):
    result += int(i)
for i in string[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)