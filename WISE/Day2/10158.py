w, h = map(int, input().split())
p, q = map(int, input().split()) # 초기 위치
t = int(input())

tx = t%(2*w)
ty = t%(2*h)
x, y = p, q
dx, dy = 1, 1
for i in range(tx):
    x+=1*dx
    if x==w or x==0:
        dx*=-1
for j in range(ty):
    y+=1*dy
    if y==h or y==0:
        dy*=-1
print(x, y)
# 시간복잡도 : O(max(w, h))
