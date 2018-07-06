class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # the length of the longest substring
        max_length = 0
        # the first index of the substring to be tested
        i = 0
        # a dict which stores the character to the current index of it
        char_dict = {}

        for j in range(len(s)):
            # if the current has been found in the dict and the current
            # is found in the testing substring(regardless of the character before i)
            if s[j] in char_dict and i < char_dict[s[j]] + 1:
                i = char_dict[s[j]] + 1
            else:
                max_length = max(max_length, j - i + 1)
            # apend the character and the index to the dict or update the current index
            char_dict[s[j]] = j

        return max_length
