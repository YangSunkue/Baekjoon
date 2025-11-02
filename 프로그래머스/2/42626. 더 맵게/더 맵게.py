import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    
    result = 0
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return result
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)

        heapq.heappush(scoville, a + (b * 2))
        result += 1
    
    return result if scoville[0] >= K else -1  