class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            n = int(str(x)[::-1])
            if n >= (2 ** 31) or n <= (-2 ** 31):
                return 0
            return n
        elif x == 0:
            return 0
        else:
            n = -int(str(x)[1:][::-1])
            if n >= (2 ** 31) or n <= (-2 ** 31):
                return 0
            return n
