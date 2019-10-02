class Solution:
    def longestPalindrome(self, s):
        def helper(i, j):
            if i == 0 or j == len(s) - 1:
                return s[i: j + 1]
            elif s[i - 1] == s[j + 1]:
                return helper(i - 1, j + 1)
            else:
                return s[i: j + 1]

        if len(s) <= 1:
            return s
        res = ""
        for i in range(len(s)):
            curr = helper(i, i)
            if len(curr) > len(res):
                res = curr
        for i in range(len(s) - 1):
            curr = helper(i, i+1)
            if len(curr) > len(res):
                res = curr
        return res

s = Solution()
string = "b"
print(s.longestPalindrome(string))

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(s, i, j):
            if i == 0 or j == len(s) - 1:
                return s[i: j + 1]
            elif s[i - 1] == s[j + 1]:
                return helper(s, i - 1, j + 1)
            else:
                return s[i: j + 1]

        if len(s) <= 1:
            return s
        k = [helper(s, i, i) for i in range(len(s))]
        k += [helper(s, i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
        res = k[0]
        for lst in k:
            if len(res) < len(lst):
                res = lst
        return res

"""
