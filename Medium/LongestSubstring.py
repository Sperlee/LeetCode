class Solution(object):
    def lengthOfLongestSubstring(self, s):
        string_max = ""

        for i in range(len(s)):
            k = i + 1
            string_test = s[i]

            while k < len(s) and s[k] not in string_test:
                string_test += s[k]
                k += 1

            if(len(string_test) > len(string_max)):
                string_max = string_test

        return len(string_max)