from collections import deque
def solution(bridge_length, weight, truck_weights):
    queue = deque(bridge_length*[0])
    truck_weights = deque(truck_weights)
    n = len(truck_weights)
    
    s = 0       # 무게
    answer = 0  # 결과값 : 날짜
    count = 0   # 나간 트럭 수
    while count!=n:
        out = queue.pop()
        s-=out
        if out != 0:
            count+=1
        
        if len(truck_weights)!=0 and s+truck_weights[0]<=weight:
            t = truck_weights.popleft()
        else:
            t = 0
        queue.appendleft(t)
        s += t
        answer += 1
    return answer