"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8

"""
from typing import List


class Solution:
    def generateParentheses(self, n: int) -> List[str]:
        ans = []

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                ans.append("".join(s))
                return ans
            if left < n:
                s.append('(')
                backtrack(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(')')
                backtrack(s, left, right+1)

        backtrack([], 0, 0)
        return ans
