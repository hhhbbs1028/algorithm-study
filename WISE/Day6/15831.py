n, b, w = map(int, input().split())
rocks = list(map(str, input().strip()))

ans, nidx = 0, 0
color = {'B' : 0, 'W': 0}
for i in range(n):
    while nidx<n and color['B']<=b:
        color[rocks[nidx]]+=1
        # print(i, nidx, color)
        if color['W']>=w and color['B']<=b:
            ans = max(ans, color['B']+color['W'])
        nidx+=1
    color[rocks[i]]-=1
print(ans)