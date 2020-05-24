# 왜 hash에 있는걸까?

# sorting을 활용한 풀이
# O(log(N) + N) = O(N)
# 정확히는 O(NK) // K는 전화번호 길이
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1]:
            return False
    return True

# trie를 활용한 풀이
