from collections import defaultdict
import sys
input = sys.stdin.readline

"""
같은 구성: 같은 문자가 같은 개수일 경우 ( 순서 상관 없음 )
비슷한 단어: 같은 구성이거나 / 한 단어에서 하나의 문자를 더하거나/빼거나/수정했을 때 같은 구성일 경우

-> 단어 길이가 3이상 차이날 경우엔 비슷한 단어가 아니다.
-> 기준 단어의 각 문자 당 개수를 구한다.
-> 대상 단어의 각 문자 당 개수와 비교하여, 그 차이가 총합 3이상일 경우 제외한다.
"""

N = int(input())
ref = input().strip()

"""기준 단어의 각 문자 당 개수 저장"""
ref_count = defaultdict(int)
for key in ref:
    ref_count[key] += 1

"""비슷한 단어 개수 세기"""
result = 0
for _ in range(N - 1):

    word = input().strip()
    diff_len = abs(len(ref) - len(word))

    if diff_len >= 2:
        continue

    word_count = defaultdict(int)
    for key in word:
        word_count[key] += 1
    
    # 모든 문자의 합집합
    all_chars = set(ref) | set(word)
    
    # 하나의 문자가 다르면 diff count 2 증가 ( 1번의 수정으로 diff count 2 감소 )
    diff_count = 0
    for char in all_chars:
        diff_count += abs(ref_count.get(char, 0) - word_count.get(char, 0))

        if diff_count > 2:
            break

    if diff_count == 0:  # 같은 단어
        result += 1
    elif diff_len == 0 and diff_count == 2:  # 길이가 같고 문자 하나가 다른 단어
        result += 1
    elif diff_len == 1 and diff_count == 1:  # 같은 단어인데 길이 차이가 1 나는 단어
        result += 1

print(result)