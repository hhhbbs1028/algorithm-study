word = list(input().strip())
alp = [ 0 for _ in range(ord('z')-ord('a')+1)]
for w in word:
    alp[ord(w.lower())-ord('a')]+=1
    
m = max(alp)
if alp.count(m)>1:
    print("?")
else:
    print(chr(alp.index(m)+ord('a')).upper())