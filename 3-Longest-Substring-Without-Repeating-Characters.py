from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sett = set()
        max_sub = left = 0

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            
            sett.add(s[right])
            max_sub = max(max_sub, right - left + 1)
        return max_sub
            
        