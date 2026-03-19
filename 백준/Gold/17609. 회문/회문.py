def is_palindrome(word):
    return word==word[::-1]
# 뒤집어도 같으면 true

t = int(input())
for _ in range(t):
    word = input()
    
    ans = 2 
    if is_palindrome(word):
        ans = 0
    else:
        l, r = 0, len(word)-1
        while l<=r:
            if word[l]!=word[r]:
                # l을 삭제한 문자열 : s[:l] + s[l+1:]
                # s[:l-1] s[r+1:] <- 두 범위는 이미 팰린드롬


                # 파이썬 슬라이싱은 끝을 포함하지 않음
                if is_palindrome(word[l+1:r+1]) or is_palindrome(word[l:r]):
                    ans = 1
                break
            l+=1
            r-=1
    print(ans)