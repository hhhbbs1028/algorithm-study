t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if (a%2==1 and b%2==1 and c%2==1):
        print(2)
    else:
        print(1)