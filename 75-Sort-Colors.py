class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        left = 0
        # on each iteration we want to sort 0s and 1s and the 2s will fall in place
        for i in range(2):
            for right in range(left,len(nums)):
                if nums[right] == i:
                    nums[right],nums[left] = nums[left],nums[right]
                    left+=1
        return nums
