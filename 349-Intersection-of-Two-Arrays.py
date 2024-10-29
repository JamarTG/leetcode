class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = []
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2:
                    res.append(i)
            return res

        for i in nums2:
            if i in nums1:
                res.append(i)
        return res
        # iterate through the one with the shorter length

        