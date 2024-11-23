class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        threshold = len(nums)
        def generate_subsets(lst,idx):
            if len(lst) == threshold:
                return [lst]
            res = []
            for i in range(idx,len(nums)):
                res += generate_subsets(lst + [nums[i]],i+1)

            return [lst] + res

        return generate_subsets([],0)

        