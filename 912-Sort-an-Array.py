class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) < 2:
            return nums

        mid = len(nums) // 2

        nums1 = self.sortArray(nums[:mid])
        nums2 = self.sortArray(nums[mid:])

        res = self.merge(nums1,nums2)

        return res

    def merge(self,nums1,nums2):
        i = j = 0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        
        while i < len(nums1):
            res.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            res.append(nums2[j])
            j += 1

        return res 
        
        