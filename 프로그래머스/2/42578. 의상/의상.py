import math
from collections import Counter
def solution(clothes):
    answer = 0
    c = []
    for a, b in clothes:
        c.append(b)
    li = list(Counter(c).values())
    for i in range(len(li)):
        li[i]+=1
    answer = math.prod(li)-1    
    return answer