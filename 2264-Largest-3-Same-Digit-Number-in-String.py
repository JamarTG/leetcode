class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr = ''
        

        # start at index where you have 2 values
        for i in range(2,len(num)):
            # ensure last 3 are equal and the num is greater than the prev number
            if num[i] == num[i - 1] == num[i - 2] and num[i] >= curr:
                # set current number as the max
                curr = num[i]
        # return the string  '777'
        return curr + curr + curr
        
        # print(curr)
            

        
