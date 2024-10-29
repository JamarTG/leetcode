from collections import Counter
from math import ceil

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # get the character frequency
        counter = Counter(nums)
        res = 0
        for el in counter:
            # (c * (c-1))// 2
            res += ceil(counter[el]  * (counter[el] - 1) / 2)
        return res






        
