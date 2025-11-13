n, m = map(int, input().split())
castle = [list(map(str, input().strip())) for _ in range(n)]

#  .은 빈칸, X는 경비원이 있는 칸이다.
no_guard_n = 0
no_guard_m = 0

for i in range(n):
    if 'X' not in castle[i]:
        no_guard_n+=1
        
for j in range(m):
    if all(castle[i][j] != 'X' for i in range(n)):
        no_guard_m += 1
print(max(no_guard_n, no_guard_m))