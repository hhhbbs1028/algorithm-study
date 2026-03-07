# 어떤 B진법 (2 ≤ B ≤ 64)으로 표현하면 회문이 되는 경우가 있는지 알려주는 프로그램
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
    
# reverse 비교 => list == list[::-1]
# 슬라이싱 : [start:stop:step]