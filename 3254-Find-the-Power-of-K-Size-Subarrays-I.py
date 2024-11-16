class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        counter = 0
        res = []
    
        for i in range(len(nums)):

            if i == 0 or k == 1 or nums[i-1] == nums[i] - 1 :
                counter += 1
            else:
                counter = 1  # Reset the counter if the sequence is broken
            
            if i < k - 1:
                continue

            
            if counter >= k:
                res.append(nums[i])

            else:
                res.append(-1)
            
        return res        