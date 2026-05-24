from collections import deque
def solution(priorities, location):
    q = deque(enumerate(priorities))
    a = []
    while len(q):
        element, priority = q.popleft()
        if len(q)==0 or priority >= max(x[1] for x in q):
            a.append(element)
        else:
            q.append((element, priority))
    print(a)
    answer = a.index(location)+1
    return answer