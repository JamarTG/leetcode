class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        left = right = 0
        res = 0

        while left < len(nums):
            if nums[left] != 0:
                left+=1
                continue

            right = left
            
            # n = 0

            while right < len(nums) and nums[right] == 0:
                right += 1
                # n += 1
            n = right - left
            res += n * (n + 1)//2

            left = right

            
            
        
            
        return res
