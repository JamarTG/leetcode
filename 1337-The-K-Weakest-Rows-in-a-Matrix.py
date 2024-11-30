import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i in range(len(mat)):
            strength = self.get_strength(mat[i])
            heapq.heappush(res, (-strength, -i))  

            if len(res) > k:
                heapq.heappop(res)

        return [abs(el[-1]) for el in sorted(res, reverse=True)]
       
    def get_strength(self,row):
        left,right = 0,len(row)

        while left < right:
            mid = (left + right) // 2
        
            if row[mid] == 0:
                right = mid 
            else:
                left = mid + 1
        return left