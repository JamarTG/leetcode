import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i in range(len(mat)):
            heapq.heappush(res, (self.get_strength(mat[i]), i))

        return [heapq.heappop(res)[-1] for i in range(k)]

    def get_strength(self, row):
        left, right = 0, len(row)
        while left < right:
            mid = (left + right) // 2
            if row[mid] == 0:
                right = mid
            else:
                left = mid + 1
        return left
