class Solution:

    def __init__(self):
        self.words = set()
        self.string = None
        self.check = dict()

    def wordBreak(self, s, wordDict):
        self.string = s
        for str in wordDict:
            self.words.add(str)
        return self.helper(0)

    def helper(self, start):
        if start == len(self.string):
            return True
        if start in self.check:
            return self.check[start]
        for end in range(start+1, len(self.string)+1):
            if (self.string[start:end] in self.words) and self.helper(end):
                self.check[start] = True
                return self.check[start]
        self.check[start] = False
        return self.check[start]

s = "leetcode"
wordDict = ["leet", "code"]
x = Solution()
print(x.wordBreak(s, wordDict))