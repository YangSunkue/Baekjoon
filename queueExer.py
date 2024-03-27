from collections import deque  # 덱, 큐와 스택의 장점을 모두 채용한 것, 원형 큐

queue = deque()

queue.append(5) 
queue.append(2)
queue.append(3)
queue.append(7)
print(queue)

queue.append(queue.popleft())
print(queue)
queue.append(queue.popleft())
print(queue)