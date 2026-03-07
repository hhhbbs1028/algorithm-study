n, k = map(int, input().split())
record = [list(map(str, input().split())) for _ in range(k)]
wheel = ['?' for _ in range(n)]

t_ch = int(record[k-1][0])
wheel[0] = record[k-1][1]
x = 0
flag = True
for i in range(1, k):
    n_ch, ch = int(record[k-i-1][0]), record[k-i-1][1]
    x = (x+t_ch)%n
    if wheel[x]=='?' or wheel[x] == ch:
        wheel[x] = ch
        t_ch = n_ch
    elif wheel[x] != ch:
        flag = False

existed_wheel = []
for w in wheel:
    if w!='?':
        if w not in existed_wheel:
            existed_wheel.append(w)
        else:
            flag = False
            break

if flag:
    for w in wheel:
        print(w, end="")
else:
    print("!")