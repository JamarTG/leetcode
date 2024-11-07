class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        
        p1 = p2 = 0

        len1 = len(nums1)
        len2 = len(nums2)

        if len1 == 0:
            return nums2
        if len2 == 0:
            return nums1


        while p1 < len1 and p2 < len2:
            if nums1[p1][0] == nums2[p2][0]:
                res.append([nums1[p1][0],nums1[p1][1] + nums2[p2][1]])
                p1 += 1
                p2 += 1
            elif nums1[p1][0] < nums2[p2][0]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        
        if p1 < len1:
            res.extend(nums1[p1:])
        if p2 < len2:
            res.extend(nums2[p2:])

        return res        