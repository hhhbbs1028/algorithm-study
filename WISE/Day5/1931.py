n = int(input())
schedule = []
for _ in range(n):
    start, end = map(int, input().split())
    schedule.append((start, end))

schedule.sort(key= lambda x:(x[1], x[0]))

cnt = 0
last_end = 0
for i in range(n):
    if schedule[i][0] >= last_end:
        cnt+=1 
        last_end = schedule[i][1]
print(cnt)