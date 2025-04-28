"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is

among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

 

Constraints:

    1 <= s.length <= 104
    s consists of lowercase English letters.

"""

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        in_stack = set()
        
        for c in s:
            counter[c] -= 1
            if c in in_stack:
                continue
            
            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)
            stack.append(c)
            in_stack.add(c)
            
        return "".join(stack)
                
                
                    