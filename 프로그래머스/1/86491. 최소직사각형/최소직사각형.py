def solution(sizes):
    w, h = 0, 0
    for a, b in sizes:
        (a,b) = (a,b) if a>b else (b,a)
        if a > w:
            w = a
        if b > h:
            h = b
    return w*h

    