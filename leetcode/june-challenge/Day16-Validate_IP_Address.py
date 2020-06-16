# Day 15 - Validate IP Address

# 그냥 구현문제로 logical하게 짰더니 너무 길어짐.
# 효율적인 방법을 찾다가 잘 짠 코드를 발견

# 배울 점
# 1. try/except 문으로 적절하게 검사하는 방법
# 2. 여러 조건을 검사할 땐 단위 하나로 쪼갠 뒤 all()로 묶어서 처리도 가능하다.
# 파이썬을 파이썬답게 쓸 수 있게 노력하자.

class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(s):
            try: return str(int(s)) == s and 0 <= int(s) <= 255
            except: return False
            
        def isIPv6(s):
            if len(s) > 4: return False
            try: return int(s, 16) >= 0 and s[0] != '-'
            except: return False

        if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")): 
            return "IPv4"
        if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")): 
            return "IPv6"
        return "Neither"