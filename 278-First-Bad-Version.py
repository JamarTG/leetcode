# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right = 0,n
     
        while left <= right:
            mid = (left + right) // 2
            res = isBadVersion(mid)
                      
            if right == left:
                return mid
        
            if res:
                right = mid
            if not res:
                left = mid + 1

        return mid