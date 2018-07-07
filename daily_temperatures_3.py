class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        length = len(temperatures)
        days = [0 for _ in range(length)]

        for i in range(length - 2, -1, -1):
            # compare with the next day first
            j = i + 1
            while True:
                if temperatures[i] < temperatures[j]:
                    days = j - i
                    break
                # temp[i] >= temp[j], if days[j] represents the next day whose temp is warmer than day j
                # if day[j] > 0 then compare the earliest day whose temp is warmer than day j with day i
                elif days[j] > 0:
                    j += days[j]
                # if days[j] == 0 means none of the following day is warmer than day j
                else:
                    break

        return days
