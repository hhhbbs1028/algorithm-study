def is_palindrome(x, base):
    
    digit = []
    
    while(x>0):
        digit.append(x%base)
        x//base
    for i in range(0, len(digit)//2):
        if digit[i] != digit[len(digit)-i-1]:
            return False
    return True
        


t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    
    for i in range(2, 65):
        if is_palindrome(n, i):
            ans = 1
            break 
    print(ans)

