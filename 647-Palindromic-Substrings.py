class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # ODD CASE

            left = right = i

            while left >= 0 and right < len(s) and s[right] == s[left]:
                res += 1
                left -= 1
                right += 1
        
            left = right = i
            right += 1

            while left >= 0 and right < len(s) and s[right] == s[left]:
                res += 1
                left -= 1
                right += 1
            
        return res