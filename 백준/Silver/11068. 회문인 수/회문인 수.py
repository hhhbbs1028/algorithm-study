def cal(number, B):
    # number를 B진수로 변환
    n = []
    while True:
        n.append(number%B)
        number=number//B
        if number < B:
            n.append(number)
            break
    n.reverse()
    return n

t = int(input())
for _ in range(t):
    flag = 0
    num = int(input())
    for i in range(64, 1, -1):
        cal_num = cal(num, i)
        # print(i, cal_num)
        if cal_num == cal_num[::-1]:
            flag = 1
            break
    print(flag)