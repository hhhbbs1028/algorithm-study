import sys
input = sys.stdin.readline
n, m, t = map(int, input().split())
k, a, b = map(int, input().split())
k = min(k, max(n,m))

life = []
for _ in range(n):
    life.append(list(input().strip()))

def plus_count(x, y):
    for i in range(-k, k+1):
        if 0<=x+i<n:
            for j in range(-k, k+1):
                if 0<=y+j<m:
                    count_life[x+i][y+j]+=1
    count_life[x][y]-=1
    
def show_graph(graph):
    for i in range(n):
        for j in range(m):
            print(graph[i][j], end="")
        print()
    print()

def born_life(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j]=='*':
                if (count_life[i][j]<a) or (count_life[i][j]>b):
                    graph[i][j]='.'
            else:
                if a<count_life[i][j]<=b:
                    graph[i][j]='*'

for _ in range(t):
    count_life = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if life[i][j]=='*':
                plus_count(i, j)
                
    born_life(life)
    # show_graph(count_life)
show_graph(life)