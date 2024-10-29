class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
    
        # find the word with the shortest length
        shortest_length = min(map(len,strs))
        constring = ''


        for i in range(shortest_length):
            l = strs[0][i]

            for word in strs:
                if word[i] != l:
                    return constring

            constring +=l
        return constring
            

    # we then check each indices for a  match in character at that index
    # when we have a match we update the string we have    # when we find a non-match we will then return the string we are at 