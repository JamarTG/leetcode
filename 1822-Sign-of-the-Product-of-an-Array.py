class Solution:
    def arraySign(self, nums: List[int]) -> int:
        

        # 0 - if we encounter a 0
        # 1 - if we have an even number of numbers below 0
        # -1 - if we have an odd number of numbers below 0
        n_count = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                n_count += 1

        if n_count & 1 == 0:
            return 1
        return -1