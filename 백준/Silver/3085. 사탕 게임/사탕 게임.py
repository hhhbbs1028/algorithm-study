def count_max(graph):
    n = len(graph)
    answer = 1
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if graph[i][j] == graph[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)
        
        cnt = 1
        for j in range(n-1):
            if graph[j][i] == graph[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)
    return answer

def print_graph(graph):
    n = len(graph)
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end = " ")
        print()
    print()
        
n = int(input())
bomboni = []
for _ in range(n):
    # 빨간색 C / 파란색 P / 초록색 Z / 노란색 Y
    bomboni.append(list(input().strip()))
    
m_count = count_max(bomboni)
for i in range(n):
    for j in range(n):
        if i+1<n:
            bomboni[i][j], bomboni[i+1][j] = bomboni[i+1][j], bomboni[i][j]
            temp_count = count_max(bomboni)
            if temp_count>m_count:
                m_count = temp_count
            bomboni[i][j], bomboni[i+1][j] = bomboni[i+1][j], bomboni[i][j]
        if j+1<n:
            bomboni[i][j], bomboni[i][j+1] = bomboni[i][j+1], bomboni[i][j]
            temp_count = count_max(bomboni)
            if temp_count>m_count:
                m_count = temp_count
            bomboni[i][j], bomboni[i][j+1] = bomboni[i][j+1], bomboni[i][j]
print(m_count)