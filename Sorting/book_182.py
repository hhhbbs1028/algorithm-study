n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# k번의 바꿔치기 연산 배열 a의 모든 원소의 합이 최대가 되도록 
# b의 가장 큰 원소 <-> a의 가장 작은 원소, 단 b>a일 때

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
        
print(sum(a))