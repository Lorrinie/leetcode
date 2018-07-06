class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        max_number = 1 << 31

        reversed_number = 0
        flag = 1

        if x < 0:
            x = -x
            flag = -1

        while x != 0:
            t = x % 10
            x //= 10
            reversed_number = reversed_number * 10 + t
            if reversed_number >= max_number:
                reversed_number = 0
                break

        return reversed_number * flag
