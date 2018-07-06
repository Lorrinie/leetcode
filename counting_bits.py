class Solution:
    def countBits(self, num):
        """
        i & (i - 1) can set the right-most '1' to '0'
        so if we do it n times, the amount of '1' is n
        result list store the amount of i, so it alse store how many times we calculate
        for example, 4 * 3 = 0, so result[4] = 1(calculate once)
        5 * 4 = 4, result[5] = result[4] + 1 = 2
        result[1] = result[1*(1-1)] + 1 = 1
        if result[i] = result[i&(i-1)] + 1, assume k&(k-1)=i
        result[k] equals the times we calculate result[i] add 1

        another solution:
        if num is an even, result is equal to num / 2
        if num is an odd, result is equal to num / 2 + 1
        :type num: int
        :rtype: List[int]
        """

        # list.add is too slow
        result = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            t = result[i & (i - 1)] + 1
            result[i] = t

        return result