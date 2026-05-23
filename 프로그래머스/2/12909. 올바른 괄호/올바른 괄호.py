def solution(s):
    answer = True
    l = []
    for c in s:
        if c=='(':
            l.append(c)
        else:
            if not l or l.pop() != '(':
                return False
                    
    return len(l)==0