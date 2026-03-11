import sys
import copy
input = sys.stdin.readline
n, m, t = map(int, input().split())
k, a, b = map(int, input().split())
k = min(k, max(m, n))
    
life = []
for _ in range(n):
    life.append(list(input().strip()))

def show_graph(graph):
    for i in range(n):
        for j in range(m):
            print(graph[i][j], end=" ")
        print()
    print()

def plus_count(x, y):
    for i in range(-k, k+1):
        if 0<=x+i<n:
            for j in range(-k, k+1):
                if 0<=y+j<m:
                    count_life[x+i][y+j]+=1
    count_life[x][y]-=1

def minus_count(x, y):
    for i in range(-k, k+1):
        if 0<=x+i<n:
            for j in range(-k, k+1):
                if 0<=y+j<m:
                    count_life[x+i][y+j]-=1
    count_life[x][y]+=1

count_life = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if life[i][j]=='*':
            plus_count(i, j)
    
for _ in range(t):  
    temp_count = copy.deepcopy(count_life)
    for i in range(n):
        for j in range(m):
            if life[i][j]=='*':
                if (temp_count[i][j]<a) or (temp_count[i][j]>b):
                    life[i][j]='.'
                    minus_count(i,j)
            else:
                if a<temp_count[i][j]<=b:
                    life[i][j]='*'
                    plus_count(i,j)
show_graph(life)