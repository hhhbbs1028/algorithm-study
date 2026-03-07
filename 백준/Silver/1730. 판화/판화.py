n = int(input())
actions = list(input().strip())
graph = [["."]*n for _ in range(n)]
a_graph = [[]*n for _ in range(n)]

def g_print(graph):
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end="")
        print()
# DURL
a = ['|', '|', '-', '-']
p = ['D', 'U', 'R', 'L']
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
x, y = 0, 0
for i in range(len(actions)):
    action = actions[i]
    a_idx = p.index(action)
    xn = x+dx[p.index(action)]
    yn = y+dy[p.index(action)] 
    
    if (0 <= xn < n) and (0 <= yn < n):
        if graph[x][y] == '.':
            graph[x][y] = a[a_idx]
        else:
            if graph[x][y] != a[a_idx]:
                graph[x][y] = '+'
        
        if graph[xn][yn] == '.':
            graph[xn][yn] = a[a_idx]
        else:
            if graph[xn][yn] != a[a_idx]:
                graph[xn][yn] = '+'
        
        x += dx[p.index(action)]
        y += dy[p.index(action)]

g_print(graph)