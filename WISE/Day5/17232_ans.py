import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
k, a, b = map(int, input().split())

life = []
for _ in range(n):
    life.append(list(input().strip()))

def calc_count():
    count = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if life[i][j] == '*':
                for di in range(-k, k+1):
                    for dj in range(-k, k+1):
                        if di==0 and dj==0:
                            continue
                        ni, nj = i+di, j+dj
                        if 0<=ni<n and 0<=nj<m:
                            count[ni][nj] += 1
    return count

for _ in range(t):
    count = calc_count()
    new_life = [row[:] for row in life]  # 얕은 복사로 충분 (1depth)
    
    for i in range(n):
        for j in range(m):
            if life[i][j] == '*':
                if count[i][j] < a or count[i][j] > b:
                    new_life[i][j] = '.'
            else:
                if a < count[i][j] <= b:
                    new_life[i][j] = '*'
    
    life = new_life

for row in life:
    print("".join(row))