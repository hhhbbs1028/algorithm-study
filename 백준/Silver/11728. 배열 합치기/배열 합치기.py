n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sort = []
i, j = 0, 0
while i<n and j<m:
    if a[i] < b[j]:
        sort.append(a[i])
        i+=1
    else:
        sort.append(b[j])
        j+=1
        
sort.extend(a[i:])
sort.extend(b[j:])
print(*sort)
