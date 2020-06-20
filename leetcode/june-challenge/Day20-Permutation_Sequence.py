# Day 20 - Permutation Sequence

# Naive & 한 줄짜리 간단한 코드
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return list(map(''.join, itertools.permutations([str(i) for i in range(1,n+1)])))[k-1]

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = range(1, n + 1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            numbers.remove(numbers[index])
        return permutation