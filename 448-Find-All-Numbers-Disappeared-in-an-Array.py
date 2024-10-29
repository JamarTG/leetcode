class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            a = abs(nums[i])
            nums[a-1] = abs(nums[a-1]) * -1

        return [b+1 for b in range(len(nums)) if nums[b] > 0]


        
        