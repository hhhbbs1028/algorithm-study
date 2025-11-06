n = [int(input()) for _ in range(9)]
ri = None
rj = None
for i in range(8):
    for j in range(i+1, 9):
        if n[i]+n[j] == sum(n)-100:
            ri = n[i]
            rj = n[j]
            break
        
n.remove(ri)
n.remove(rj)
n.sort()
for e in n:
    print(e)
