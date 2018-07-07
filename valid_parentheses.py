class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_dict = {'(': ')', '[': ']', '{': '}'}
        left_set = {'(', '[', '{'}
        stack = []

        for c in s:
            if c in left_set:
                stack.append(c)
            elif stack and c == p_dict[stack[-1]]:
                stack.pop()
            else:
                return False

        if stack:
            return False
        else:
            return True