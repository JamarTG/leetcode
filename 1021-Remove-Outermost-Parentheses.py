class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        depth = 0
        res = ''
        for i in range(len(s)):
            
            
            
            if s[i] == "(":
                depth += 1

                if depth != 1:
                    res += s[i]
            else:
                depth -= 1

                if depth != 0:
                    res += s[i]
        return res
            
        