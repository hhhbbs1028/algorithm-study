from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
    
visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)

def dfs(first):
    visited_dfs[first] = True
    print(first, end=' ')
    
    for node in graph[first]:
        if not visited_dfs[node]:
            dfs(node)

def bfs(first):
    queue = deque([first])
    visited_bfs[first] = True
    
    while queue:    
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True
        

dfs(v)
print("")
bfs(v)