from collections import defaultdict

# Key lesson - Use the size of the dictionary to check for duplicates given a size

class Solution:

    # The concept learnt here is using the size of the dictionary to determine if there are duplicates
    
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        counter = defaultdict(int)
        summ = sum(nums[:k])

        for i in range(k):
            counter[nums[i]] += 1 

        if len(counter) == k:
            res = max(res,summ)

        for i in range(1,len(nums)-k+1):
            summ -= nums[i-1]
            summ += nums[i+k-1]

            counter[nums[i-1]] -= 1 
            counter[nums[i+k-1]] += 1

            if counter[nums[i-1]] == 0:
                del counter[nums[i-1]] 

            if len(counter) == k:
                res = max(res,summ)
        return res
            
    