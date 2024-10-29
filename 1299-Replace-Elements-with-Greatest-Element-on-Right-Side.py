class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # get running max
        running_max = -1

        # traverse in reverse
        for i in range(len(arr)-1,-1,-1):
            # overwrite value with largest so far
            tmp = arr[i]
            arr[i] = running_max
            if tmp > running_max:
                running_max = tmp
        # return new array
        return arr
        

        
