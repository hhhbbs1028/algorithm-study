import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        if len(scoville) >= 2:
            s1, s2 = heapq.heappop(scoville), heapq.heappop(scoville)
        else:
            return -1
        heapq.heappush(scoville, s1+s2*2)
        count += 1
    return count