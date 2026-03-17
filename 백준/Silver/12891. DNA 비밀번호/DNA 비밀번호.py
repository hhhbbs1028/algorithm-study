s, p = map(int, input().split())
DNA = list(map(str, input().strip()))
A, C, G, T = map(int, input().split())

ans = 0
acgt = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
for i in range(p-1):
    acgt[DNA[i]]+=1

for i in range(s):
    j = i + p - 1
    if j<s:
        acgt[DNA[j]]+=1
        if acgt['A'] >= A and acgt['C'] >= C and acgt['G'] >= G and acgt['T'] >= T:
            ans += 1
        acgt[DNA[i]]-=1
    
print(ans)
        