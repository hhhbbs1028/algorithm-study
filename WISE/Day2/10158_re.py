w, h = map(int, input().split())
p, q = map(int, input().split()) # 초기 위치
t = int(input())

x = (p+t)%(2*w)
y = (q+t)%(2*h)
if x>w:
    x = -x+2*w
if y>h:
    y = -y+2*h
print(x, y)