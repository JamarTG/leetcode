from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        # show how to implement after
        counter = Counter(s)

        lngest= 0
        odd_count_exists = False
        for element in counter:
            if counter[element] % 2 == 0:
                lngest += counter[element]
            else:
                lngest += counter[element] - 1
                odd_count_exists = True

       

        if not odd_count_exists:
            return lngest
        return lngest + 1
        