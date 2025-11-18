t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    paint = [input() for _ in range(h)]
    
    row, col = 0, 0
    for i in range(h):
        if paint[i][0] =='#':
            f_row = True
            for j in range(w):
                if paint[i][j]!="#":
                    f_row = False
            if f_row:
                row +=1
                
    for i in range(w):
        if paint[0][i] =='#':
            f_col = True
            for j in range(h):
                if paint[j][i]!="#":
                    f_col = False
            if f_col:
                col += 1
    if row+col == h+w:
        print(min(row, col))
    else:
        print(row+col)