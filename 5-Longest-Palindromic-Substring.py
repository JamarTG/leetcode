class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        
        for i in range(len(s)):
            # ODD CASE
            right = left = i
            
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1

            left += 1
            right -= 1

            # Mistake #1: Ensure you specify key for determining max as the length
            res = max(res,s[left:right+1],key=len)

            # EVEN CASE
            left = i
            right = left + 1
            
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            
            left += 1
            right -= 1
            # Mistake #2: Ensure you account for going left being 1 less and right being 1 more
            res = max(res,s[left:right+1],key=len)
                
        return res