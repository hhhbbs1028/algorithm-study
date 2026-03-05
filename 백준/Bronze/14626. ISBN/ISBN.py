isbn = input()
w = [1, 3]
c = 0
s_idx = 0

for i in range(len(isbn)):
    if isbn[i] == '*':
        s_idx = i
    else:
        c += int(isbn[i]) * w[i % 2]

for k in range(10):
    if (c + k * w[s_idx % 2]) % 10 == 0:
        print(k)
        break