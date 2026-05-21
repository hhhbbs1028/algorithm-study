def solution(phone_book):
    answer = True
    hash_map = {}
    for phone in phone_book:
        hash_map[phone]=1
    for phone_number in hash_map:
        temp = ""
        for phone_char in phone_number: 
            temp+=phone_char
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer