t = int(input())
for _ in range(t):
    h,w,n = map(int, input().split())
    if n%h==0:
        floor = h
    else:
        floor = n%h
    ho = (n-1)//h+1
    print(floor*100+ho)