n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

s = sum(l)

top = 0
for i in range(n):
    d_ij = 0
    temp_ij = 0
    for j in range(i, n-1):
        temp_ij += l[j]
        d_ij = min(s-temp_ij, temp_ij)
        top = max(top, d_ij)
print(top)