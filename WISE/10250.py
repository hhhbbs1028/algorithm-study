t = int(input())
tc = [list(map(int, input().split())) for _ in range(t)]

# for _ in range(t):
#     h,w,n = map(int, input().split())
#     print(n//h, n%h)
# print(tc)

for c in tc:
    h,w,n = c[0],c[1],c[2]
    if n%h==0:
        cmd = h
    else:
        cmd = n//h 
    print((cmd)*100+n%h+1)