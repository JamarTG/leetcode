from collections import Counter
from math import ceil

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)

        res = 0
        for el in counter:
            res += ceil(counter[el]  * (counter[el] - 1) / 2)
        return res






        