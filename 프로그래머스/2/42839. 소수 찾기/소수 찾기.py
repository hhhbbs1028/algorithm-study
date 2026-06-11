from itertools import permutations
def solution(numbers):
    
    def is_prime(number):
        if number==1 or number<=0:
            return False        
        for i in range(2, int(n**0.5)+1):
            if number%i==0:
                return False
        return True
    
    numbers = list(numbers.strip())
    
    created_numbers = set()
    for i in range(1, len(numbers)+1):
        for x in list(permutations(numbers, i)):
            created_numbers.add(int(''.join(x)))
    print(created_numbers)
    
    answer = 0
    for n in created_numbers:
        if is_prime(n):
            answer+=1
    
    return answer