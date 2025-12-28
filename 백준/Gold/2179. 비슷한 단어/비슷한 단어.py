import sys
input = sys.stdin.readline

def check(word1, word2):
    """두 단어의 공통 접두사 반환"""
    prefix_chr = []
    for i in range(min(len(word1), len(word2))):
        if word1[i] == word2[i]:
            prefix_chr.append(word1[i])
        else:
            break
    return ''.join(prefix_chr)

N = int(input())
words = []
for i in range(N):
    s = input().strip()
    words.append((s, i))  # 단어, 우선순위
words.sort()

prefix_dict = dict()  # prefix별로 해당 prefix를 갖는 단어들 저장
max_ln = 0
prefix_list = []  # 최대 길이 prefix들 저장

for i in range(1, N):
    prefix = check(words[i][0], words[i - 1][0])
    prefix_len = len(prefix)

    if prefix_len < max_ln:
        continue

    # 더 긴 prefix를 찾으면 초기화
    if prefix_len > max_ln:
        prefix_list = []
        max_ln = prefix_len
    
    prefix_list.append(prefix)

    # prefix_dict에 해당 prefix를 가진 단어들 추가
    if prefix not in prefix_dict:
        prefix_dict[prefix] = set()
    
    prefix_dict[prefix].add((words[i][1], words[i][0]))  # (우선순위, 단어)
    prefix_dict[prefix].add((words[i-1][1], words[i-1][0]))

# 최대 길이 prefix들 중에서 가장 먼저 입력된 조합 찾기
result_idx = N
result = None

for prefix in prefix_list:
    # 해당 prefix를 가진 단어들 중 우선순위대로 앞 2개 선택
    first, second = sorted(prefix_dict[prefix])[:2]

    # 첫 번째 단어의 우선순위가 더 앞이면 갱신
    if first[0] < result_idx:
        result = (first[1], second[1])
        result_idx = first[0]

print(result[0])
print(result[1])