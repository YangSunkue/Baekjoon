from collections import deque

def solution(st):

    def is_correct(string):
        stack = []

        for s in string:
            # 열린 괄호일 경우
            if s == '[' or s == '{' or s == '(':
                stack.append(s)
                continue
            
            # 닫힌 괄호일 경우
            if len(stack) == 0:
                return False
            
            pop_data = stack.pop()
            if (s == ']' and pop_data != '[') or (s == '}' and pop_data != '{') or (s == ')' and pop_data != '('):
                return False
        
        if len(stack) == 0:
            return True
    
    # 덱에 문자열 넣기
    queue = deque([])
    for s in st:
        queue.append(s)
    
    # 회전하며 올바른 괄호인지 검사
    result = 0
    if is_correct(''.join(queue)):
        result += 1
    for i in range(len(st) - 1):
        item = queue.popleft()
        queue.append(item)

        if is_correct(''.join(queue)):
            result += 1

    return result