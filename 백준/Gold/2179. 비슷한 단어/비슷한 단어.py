import sys
input = sys.stdin.readline

N = int(input())
words = []
for priority in range(N):
    words.append((input().strip(), priority))  # (단어, 우선순위)
words.sort()

def get_prefix(word1, word2):
    prefix = []
    for i in range(min(len(word1), len(word2))):
        if word1[i] == word2[i]:
            prefix.append(word1[i])
        else:
            break
    return ''.join(prefix)
    
prefix_dict = dict()
max_length = 0
prefix_list = []

for i in range(1, N):
    prefix = get_prefix(words[i][0], words[i - 1][0])
    length = len(prefix)

    if max_length > length:
        continue

    if max_length < length:
        prefix_list = []
        max_length = length
    
    prefix_list.append(prefix)

    if prefix not in prefix_dict:
        prefix_dict[prefix] = set()
    
    prefix_dict[prefix].add((words[i][1], words[i][0]))  # (우선순위, 단어)
    prefix_dict[prefix].add((words[i - 1][1], words[i - 1][0]))

result_priority = N
result = None
for prefix in prefix_list:
    first, second = sorted(prefix_dict[prefix])[:2]

    if first[0] >= result_priority:
        continue

    result_priority = first[0]
    result = (first[1], second[1])

print(result[0])
print(result[1])