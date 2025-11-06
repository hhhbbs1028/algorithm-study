x = int(input())
n = int(input())
staffs = []
score = {}
score_T = []
for _ in range(n):
    name, v = input().split()
    if int(v)>=x*0.05:
        staffs.append((name, int(v)))
        score[name]=[]

for staff in staffs:
    for i in range(1, 15):
        score[staff[0]].append(staff[1]/i)
        score_T.append(staff[1]/i)

score_f = {}
for staff in staffs:
    score_f[staff[0]]=0
    
score_T.sort(reverse=True)
for i in range(14):
    m = score_T[i]
    for staff in staffs:
        if m in score[staff[0]]:
            score_f[staff[0]]+=1

for s in sorted(score_f):
    print(s, score_f[s])