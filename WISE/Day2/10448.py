# Tn = n(n+1)/2
n = int(input())
test = [int(input()) for _ in range(n)]

# 3개의 삼각수의 합으로 표현될수 있다면 1을, 그렇지 않다면 0을 출력한다.
tr = []
for i in range(1, 46):
    tr.append(int(i * (i + 1) // 2))

# print(tr)

for t in test:
    m_i = 0
    flag =0
    
    for i in range(len(tr)):
        if tr[i]>t:
          m_i=i
          break
      
    for i in range(m_i):
        for j in range(i, m_i):
            for k in range(j, m_i):
                if tr[i]+tr[j]+tr[k]==t:
                    flag=1
                    break
    print(flag)