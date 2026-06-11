def solution(answers):
    answer = []
    c1 = [1, 2, 3, 4, 5]
    c2 = [2, 1, 2, 3, 2, 4, 2, 5]
    c3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0 for i in range(4)]
    for i in range(len(answers)):
        a = answers[i]
        if c1[i%5] == a:
            count[1]+=1
        if c2[i%8] == a:
            count[2]+=1
        if c3[i%10] == a:
            count[3]+=1
    m = max(count)
    for i in range(1,4):
        if count[i]==m:
            answer.append(i)
    return answer