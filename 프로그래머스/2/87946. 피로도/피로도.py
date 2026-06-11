from itertools import permutations
def solution(k, dungeons):
    # k : 현재 피로도
    # dungeons : [[80,20],[50,40],[30,10]]
    l_duns = list(permutations(dungeons, len(dungeons)))
    answer = -1
    for duns in l_duns:
        p = k
        a = 0
        for dun in duns:
            need, consume = dun
            if p >= need:
                p -= consume
                a += 1
        answer = max(a, answer)
    return answer