class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        
        nums.sort(reverse = True)   
        max_freq = 0



        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            j = i + 1
            operations = k

            while operations >= 0 and j < len(nums):

                operations -= nums[i] - nums[j]
            
                if operations < 0:
                    break

                j+=1
            
            max_freq = max(max_freq, j - i)

        return  max_freq