import math
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

tx = t%(2*w)
ty = t%(2*h)

x, y = 1, 1
for i in range(tx):
    p += x
    if p==w or p==0:
        x*=-1

for i in range(ty):
    q += y
    if q==h or q==0:
        y*=-1

print(p,q)
