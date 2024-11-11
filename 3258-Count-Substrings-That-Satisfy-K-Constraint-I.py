class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        
        # SLIDING WINDOW (BETTER HOPEFULLY) O(n^2)
        res = 0
        left, right = 0, 0

        while right < len(s):
            wndow = s[left:right+1]

            if wndow.count("1") <= k or wndow.count("0") <= k: 
                right += 1
                res += 1
            else:
                left += 1
                right = left
            
            if right >= len(s) and left < len(s)-1:
                left  += 1 
                right = left

        return res        
        
        
        # O(N^3)  SOLUTIONS
        # res = 0

        # for i in range(len(s)):
        #     c = ''

        #     for j in range(i,len(s)):
                
        #         c += s[j]

        #         if c.count("1") > k and c.count("0") > k:
        #             break
            
        #         res += 1
        
        # return res

        # O(n^2 * m)
        # O(1)