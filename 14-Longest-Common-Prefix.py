class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs)
        for st in strs:
            i = 0
            # while the characters are equal we increment i
            while i < len(prefix) and i < len(st) and prefix[i] == st[i]:
                i+=1
            # when that is not true, we take the characters upto that point
            prefix = prefix[:i] 
        # return the prefix at the end
        return prefix

        