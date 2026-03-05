isbn = input()
w = [1, 3]
c = 0
s = 0
for i in range(len(isbn)):
    if isbn[i]!="*":
        c+=int(isbn[i])*w[i%2]
    else:
        s = i

for j in range(10):
    if (c+j*w[s%2])%10==0:
        print(j)
        break