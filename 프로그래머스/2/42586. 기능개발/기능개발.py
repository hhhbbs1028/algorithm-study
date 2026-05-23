import math
def solution(progresses, speeds):
    answer = []
    days = []
    n = len(progresses)
    for i in range(n):
        progress, speed = progresses[i], speeds[i]
        days.append(int(math.ceil((100-progress)/speed)))
        
    print(days)
    temp = days[0]
    count = 1
    for i in range(1, n):
        if days[i] <= temp:
            count+=1
        else:
            answer.append(count)
            count = 1
            temp = days[i]
    answer.append(count)
    return answer