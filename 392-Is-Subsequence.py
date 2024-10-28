class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        #while we are not at the end of both
        while i < len(s) and j < len(t):
            # check if the characters are equal
            if s[i] == t[j]:
                # move along in s
                i += 1
            # move along in t
            j += 1
        # did we reach the end of s?
        return i == len(s)

        