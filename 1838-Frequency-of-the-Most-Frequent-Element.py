class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        
        nums.sort(reverse = True)   
        max_freq = 0
        L = len(nums)


        for i in range(L):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            j = i + 1
            operations = k
            freq = 1

            while operations >= 0 and j < L:
                
                amount_needed = nums[i] - nums[j]

                if operations - amount_needed >= 0:
                    operations -= amount_needed
                    freq +=1
                else:
                    break

                j+=1
            
            max_freq = max(max_freq, j - i)

        return  max_freq