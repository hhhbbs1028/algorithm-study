n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sort = []
i, j = 0, 0
while i<n and j<m:
    if a[i] < b[j]:
        sort.append(a[i])
        i+=1
    else:
        sort.append(b[j])
        j+=1
        
sort.extend(a[i:])
sort.extend(b[j:])
print(*sort)

# 리스트에 리스트를 더할 때 : extend 활용
# * : 언패킹 연산자, 리스트 요소들을 개별 인자로 풀어서 전달
# print(*sort, sep="\n") / func(*nums) 이런 식으로 활용 가능