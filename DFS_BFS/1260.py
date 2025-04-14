from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start: int):
    visited_dfs[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True

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