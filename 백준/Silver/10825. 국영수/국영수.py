# 실버4 -> 정렬

score = []
for i in range(int(input())):
    score.append(list(input().split()))
sorted_score = sorted(score, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for name in sorted_score:
    print(name[0])