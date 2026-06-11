def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        if yellow%i==0:
            h = i + 2
            w = int(yellow//i) + 2
            if w*h-yellow==brown:
                return [w,h]
    answer = []
    return answer