def solution(n, words):
    
    """
    탈락 시 [번호, 차례] 리턴
    1. 중복된 단어
    2. 이어지지 않는 단어
    """
    
    word_set = {words[0]}
    prev = words[0][-1]
    for i in range(1, len(words)):
        
        word = words[i]
        
        if (word in word_set) or prev != word[0]:
            num = (i % n) + 1
            turn = (i // n) + 1
            return [num, turn]
        
        word_set.add(word)
        prev = word[-1]
    
    return [0, 0]