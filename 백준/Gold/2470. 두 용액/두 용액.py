import sys
input = sys.stdin.readline
n = int(input())
m = list(map(int, input().split()))

m.sort()

sum_m = 2000000001
i, j = 0, n-1
a, b = 0, 0
while i<j<n:
    sum_temp = m[i]+m[j]
    if abs(sum_temp) < abs(sum_m):
        sum_m = sum_temp
        a, b = m[i], m[j]
    if sum_temp < 0:
        i+=1
    elif sum_temp > 0:
        j-=1
    else:
        break
print(a, b)