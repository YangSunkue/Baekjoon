import sys
input = sys.stdin.readline

"""
N 이하 빨강/파랑 카드 M개씩 고르기
철수: N이하 모든 카드 낼수있음 중복가능
민수: 철수를 이기는 가장 작은 카드를 냄

KlogN: 220,000
N: 4,000,000
NlogN: 88,000,000

attack[i]보다 큰 카드 중 가장 작은 카드 찾기
1. cards 정렬
2. 이분탐색으로 가장 작은 카드 찾기
3. union find로 미사용 카드 찾기
"""
def binary_search(attack):
    """철수를 이기는 가장 작은 카드 인덱스를 반환"""
    idx = float('inf')

    left = 0
    right = M - 1
    while left <= right:
        mid = (left + right) // 2

        if attack < cards[mid]:
            idx = min(idx, mid)
            right = mid - 1
        else:
            left = mid + 1

    return idx

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

N, M, K = map(int, input().split())
cards = list(map(int, input().split()))  # 민수가 보유한 카드 (4,000,000)
attacks = list(map(int, input().split()))  # 철수의 공격 (10,000)
cards.sort()

parent = [i for i in range(M)]

for attack in attacks:

    idx = binary_search(attack)
    available_idx = find(idx)

    print(cards[available_idx])

    if available_idx + 1 < M:
        parent[available_idx] = available_idx + 1