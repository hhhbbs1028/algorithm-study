n, m = map(int, input().split())
s = set([])
for _ in range(n):
    s.add(input())
count = 0
for _ in range(m):
    word = input()
    if word in s:
        count += 1
print(count)