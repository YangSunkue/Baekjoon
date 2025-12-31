from collections import defaultdict

N = int(input())

count = defaultdict(int)
for _ in range(N):
    name = input().strip()
    count[name[0]] += 1

result = []
for key in count:
    if count[key] >= 5:
        result.append(key)
      
print(''.join(sorted(result))) if result else print('PREDAJA')