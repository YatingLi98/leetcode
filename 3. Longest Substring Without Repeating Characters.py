class Solution:
    s = None

    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)
        self.s = s
        table = set()
        index = len(s) // 2
        l1 = self.helper(index, index, table, 0)
        return max(self.lengthOfLongestSubstring(s[:index]), self.lengthOfLongestSubstring(s[index:]),
                   self.helper(index, index, table, 0))

    def helper(self, start, end, table, size):
        if start < 0 or 

s = Solution()
string = "abcabcbb"
print(s.lengthOfLongestSubstring(string))