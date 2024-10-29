class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr = ''
        
        for i in range(2,len(num)):
            if num[i] == num[i - 1] == num[i - 2] and num[i] >= curr:
                curr = num[i]

        return curr + curr + curr
        
        # print(curr)
            

        