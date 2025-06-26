from collections import defaultdict
import sys
input = sys.stdin.readline

"""
1. 자주 나오는 단어
2. 단어 길이
3. 사전 순

lambda로 정렬하기
나오는횟수: N순회하면서 딕셔너리에 나오는횟수 저장
길이: len(단어) 하면 O(1) 가능
사전순을 위한 단어: 그냥 저장
"""

N, M = map(int, input().split())

"""길이가 M 이상인 단어만 추출"""
words = []
for _ in range(N):

    word = input().rstrip()
    if len(word) >= M:
        words.append(word)


"""각 단어 등장 횟수 저장"""
word_to_count = defaultdict(int)
for word in words:
    word_to_count[word] += 1

"""[나오는 횟수, 단어] 형태로 저장"""
note = []
for word in word_to_count:
    note.append([word_to_count[word], word])

"""알파벳 정렬 후 등장횟수, 단어길이 역순으로 정렬"""
note.sort(key = lambda x: x[1])
note.sort(key = lambda x: (x[0], len(x[1])), reverse = True)

for word in note:
    print(word[1])