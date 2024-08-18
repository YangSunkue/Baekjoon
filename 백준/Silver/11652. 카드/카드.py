import sys
input = sys.stdin.readline

N = int(input()) # 카드 개수
cards = {}

for _ in range(N):

    # 카드를 key로 등록하고 등장할 때마다 value를 1씩 증가시킨다
    num = int(input())
    if num in cards:
        cards[num] += 1
    else:
        cards[num] = 1

# items()를 붙여 튜플 형태로 변환한다. 딕셔너리를 정렬하기 위해 필요한 작업.
# -x[1] : -를 붙이면 내림차순 정렬을 하게 된다.
sortedCards = sorted(cards.items(), key=lambda x: (-x[1], x[0]))
print(sortedCards[0][0])