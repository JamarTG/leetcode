class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        running_max = -1

        for i in range(len(arr)-1,-1,-1):
            tmp = arr[i]
            arr[i] = running_max
            if tmp > running_max:
                running_max = tmp
        return arr
        

        