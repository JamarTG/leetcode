class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}

        for i in range(len(s)):
            char = s[i]
            if char not in counter:
                counter[char] = [i,1]
            else:
                counter[char][1] += 1
        
        for char in counter:
            if counter[char][1] == 1:
                return counter[char][0]
        return -1

