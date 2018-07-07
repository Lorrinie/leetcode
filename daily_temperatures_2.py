class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        length = len(temperatures)
        # an increasing list of temperatures, store the index of it
        stack = []
        days = [0 for _ in range(length)]

        for i in range(length - 1, -1, -1):
            # temp[stack[-1]] <= temp[i] means temp[stack[-1]]
            # can't be the earliest day whose temp is warmer than temp[i]
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            # if stack exists, the top of it stores the earliest day whose temp is warmer than temp[i]
            # if stack is none, there is no temperature warm than temp[i]
            if stack:
                days[i] = stack[-1] - i
            stack.append(i)

        return days
