t = int(input())
for _ in range(t):
    word = input()
    # 한 문자를 삭제하여 회문으로 만들 수 있는 문자열
    # 회문0 / 유사회문1 / 그외2
    n = len(word)
    j, ans = n-1, 0
    for i in range(n):
        # print("=============")
        while i<j<n and ans<=2:
            print(i,j)
            if word[i]==word[j]:
                j-=1
                break
            else:
                if word[(i+1)%n]==word[j] and word[i]==word[j-1]:
                    if word[(i+2)%n]==word[j-1]:
                        ans+=1
                    elif word[(i+1)%n]==word[j-2]:
                        ans+=1
                        j-=1
                else:
                    ans=2
                break
    print(min(2, ans))