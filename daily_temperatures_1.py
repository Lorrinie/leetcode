class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        length = len(temperatures)
        days = [0 for _ in range(length)]
        # use 102 because when temp is 100 temp+1~max_temp is 101~101
        next = [float('inf') for _ in range(102)]

        for i in range(length - 1, -1, -1):
            # get the minimum of all the index of the temperature warmer than T[i]
            warmer_index = min(next[t] for t in range(temperatures[i] + 1, 102))
            # if warmer temperature exists in following days
            if warmer_index < float('inf'):
                days[i] = warmer_index - i
            # record the index of temperature i
            next[temperatures[i]] = i

        return days