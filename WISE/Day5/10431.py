p = int(input())
for _ in range(p):
    h = list(map(int, input().split()))[1:]
    sorted_h = [] 
    sorted_h.append(h[0])
    
    count = 0
    for i in range(1, 20):
        # 정렬할 값 : h[i]
        for j in range(i):
            if h[i] < sorted_h[j]:
                sorted_h.insert(j, h[i])
                count += i-j
                break
        if h[i] not in sorted_h:
            sorted_h.append(h[i])
    print(_+1, count)