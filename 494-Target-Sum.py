class Solution(object):
    def findTargetSumWays(self, nums, target):
        \\\
        :type nums: List[int]
        :type target: int
        :rtype: int
        \\\
       
        memo = {}
       
        def backtrack(i,summ):
            if i == len(nums)-1:
                return 1 if summ == target else 0
            
            if (i,summ) in memo:
                return memo[(i,summ)]
       

            memo[(i,summ)] = backtrack(i+1,summ + ( -1 * nums[i])) + backtrack(i+1,summ + ( 1 * nums[i]))
            
            return memo[(i,summ)]
            
        return backtrack(-1,0)
        # return self.count
        
