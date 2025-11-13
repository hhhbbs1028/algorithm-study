import sys
input = sys.stdin.readline
n = int(input())
people = []
for _ in range(n):
    name, log = list(map(str, input().split()))
    if log=="enter":
        people.append(name)
    if log=="leave":
        people.remove(name)
people.sort(reverse=True)
for p in people:
    print(p)