n = int(input())
actions = list(input().strip())
graph = [["."]*n for _ in range(n)]
a_graph = [[]*n for _ in range(n)]
# print(graph)
# 수직 방향으로 지난 점은 '|'
# 수평 방향으로만 지난 점은 '-'
# 수직과 수평 방향 모두로 지난 점은 '+'로 표기
# 격자 바깥으로 나가도록 하는 움직임 명령을 만나면, 무시하고 그 다음 명령을 진행한다.

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