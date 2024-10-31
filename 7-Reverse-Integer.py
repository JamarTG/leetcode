class Solution:
    def reverse(self, x: int) -> int:
        negative = -1 if x < 0 else 1

        x = abs(x)

        new_x = 0

        while x:
            new_x= new_x * 10 + (x % 10)
            x //=10
        
        # account for being larger than max int
        if new_x > (2**31) - 1:
            return 0

        return new_x * negative  
        