# 70. Climbing Stairs

# 계단을 1, 2단씩 밖에 올라오지 못한다면 n번째 계단에 올라올 수 있는 방법은
# n-1, n-2번째 계단에서 각각 2, 1단씩 올라온 경우의 수 밖에 없다.
# 즉 점화식을 세우면 f(n) = f(n-1) + f(n-2)로 피보나치와 같다.
# 피보나치의 경우 메모리 사용을 줄이기 위해 다음과 같이 변수 2개로 구현이 가능하다.

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b