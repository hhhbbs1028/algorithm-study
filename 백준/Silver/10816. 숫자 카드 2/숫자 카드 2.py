n = int(input())
arrN = list(map(int, input().split()))
m = int(input())
arrM = list(map(int, input().split()))

minus = [0]*(10000001)
plus = [0]*(10000001)
zero = 0

for number in arrN:
    if number > 0:
        plus[number]+=1
    elif number < 0:
        minus[-number]+=1
    else:
        zero+=1

for number in arrM:
    ans = None
    if number>0:
        ans = plus[number]
    elif number<0: 
        ans = minus[-number]
    else:
        ans = zero
    print(ans, end=" ")
        