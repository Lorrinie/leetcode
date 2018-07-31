class Solution:
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [1, 2, 2]
        i = 3

        while len(s) < n:
            # var is the number to be add
            var = 3 - s[-1]
            # s[i - 1] is the number of var to be add
            s.extend([var] * s[i - 1])
            i += 1

        return s[:n].count(1)

s1 = Solution()
s1.magicalString(4)