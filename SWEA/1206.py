for j in range(10):
    n = int(input())
    buildings = list(map(int, input().split()))
    cnt=0
    for i in range(2, len(buildings)-2):
        m_height = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        if m_height<buildings[i]:
            cnt+=buildings[i] - m_height
    print("#%d %d"%(j+1, cnt))
