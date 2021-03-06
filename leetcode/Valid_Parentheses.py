# 20. Valid Parentheses
# Stack을 활용해서 풀면 O(N)으로 가능

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                stk.append(bracket)
            else:
                if len(stk) == 0:
                    return False
                elif (stk[-1] == '(' and bracket == ')')\
                or (stk[-1] == '[' and bracket == ']')\
                or (stk[-1] == '{' and bracket == '}'):
                    stk.pop()
                else:
                    return False
        return True if not stk else False