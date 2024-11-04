class Solution:
    def maxScore(self, s: str) -> int:

        # 011101

        # 001101

        # some value -> 

        # At index 0: 1 4 
        # At index 1:
            # if we see a "1" -> right - 1
            # if we see a "0" -> left + 1
        
        max_ = 0
        left = 0
        right  = s.count("1")

        for i in range(len(s)-1):
            if s[i] == "1":
                right -= 1
            if s[i] == "0":
                left += 1

            max_ = max(max_,left + right)
        return max_





        