s = input()
p = input()

# ababa
# bab
idx, ans = 0, 0
max_idx = len(s)-len(p)+1
for idx in range(max_idx):
    si = idx
    match = True
    for ch in p:
        if s[si]==ch:
            si+=1
        else:
            match=False
            break
    if match:
        ans += 1
        idx += len(p)-1
print(ans)