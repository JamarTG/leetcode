class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        L = len(nums)

        def permutation(cur):
            if len(cur) == L:
                self.res.append(cur[:])

            for i in range(len(nums)):
                if nums[i] not in cur:
                    cur.append(nums[i])
                    permutation(cur)
                    cur.pop()

        permutation([])
        return self.res
