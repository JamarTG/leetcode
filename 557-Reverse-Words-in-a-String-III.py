class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        string = ''

        for char in s:
            if char == \ \:
                res.append(string)
                string = '' 
            else:
                string = char + string

        res.append(string)

        return \ \.join(res)