# 실버4, 정렬

score = []
for i in range(int(input())):
    data = list(input().split())
    # 점수를 int로 변환
    data[1], data[2], data[3] = int(data[1]), int(data[2]), int(data[3])

    score.append(data)

# 다중 조건 정렬
sorted_score = sorted(score, key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 정렬된 이름 출력
for name in sorted_score:
    print(name[0])