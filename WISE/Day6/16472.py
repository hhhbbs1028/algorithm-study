n = int(input())
arr = list(map(str, input().strip()))

l = len(arr)
j, ans, cnt = 0, 0, 0
c = [0]*26
for i in range(l):
    while i<=j<l and cnt<=n:
        idx = ord(arr[j])-ord('a')
        if c[idx]==0:
            cnt+=1
        c[idx] += 1
        
        if cnt>n:
            c[idx] -= 1
            if c[idx] == 0:
                cnt -= 1
            break
        j+=1
    
    ans = max(ans, j-i)
    i_idx = ord(arr[i])-ord('a')
    c[i_idx]-=1
    if c[i_idx]==0:
        cnt-=1
print(ans)