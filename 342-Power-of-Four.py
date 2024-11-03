class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        c = 0
        even = True

        if n == 0:
            return False

        while n:
            a = (n & 1)
            c += a

            if (a == 1 and not even) or c > 1:
                return False

            even = not even
            n >>= 1

        return True

