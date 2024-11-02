class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sett = set()
        left = 0

        for right in range(len(nums)):
            if nums[right] not in sett:
                nums[left],nums[right] = nums[right],nums[left]
                sett.add(nums[left])
                left += 1
        return left