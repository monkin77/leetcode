from typing import *

"""
Validate Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
"""
class Solution:
    openParenthesis = "{[("
    closeParenthesis = ")]}"

    parenthesisMap: Dict[str, str] = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    def isValid(self, s: str) -> bool:
        stack = []  # Use a list as a Stack

        for c in s:
            if c in self.openParenthesis:
                stack.append(c)
            elif c in self.closeParenthesis:
                if len(stack) > 0 and self.parenthesisMap[c] == stack.pop():
                    continue
                else:
                    # Incorrect parenthesis closure
                    return False
        
        return len(stack) == 0

res = Solution()

input1 = "[]"
input2 = "([{}])"
input3 = "[(])"

sol = res.isValid(input3)

print("Solution: ", sol)