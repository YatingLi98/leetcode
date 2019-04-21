class Solution:
    dictionary = {}

    def generateParenthesis(self, n):
        if n == 1:
            return ["()"]
        if n in self.dictionary:
            return self.dictionary[n]
        res = set()
        result = []
        for i in range(1, n):
            s1 = self.generateParenthesis(i)
            s2 = self.generateParenthesis(n - i)
            for l1 in s1:
                for l2 in s2:
                    make = l1 + l2
                    if make not in res:
                        result.append(make)
                        res.add(make)
        r = self.generateParenthesis(n - 1)
        result.extend(["(" + l + ")" for l in r])
        self.dictionary[n] = result
        return result


expected4 = ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()",
             "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]

expected3 = ["((()))", "(()())", "(())()", "()(())", "()()()"]

s = Solution()
o = s.generateParenthesis(4)
print(len(o), len(expected4))
print(o)
print(expected3)


def check(output, expected):
    res = []
    for l1 in expected:
        flag = True
        for l2 in output:
            if l1 == l2:
                flag = False
        if flag:
            res.append(l1)
    return res


print(check(o, expected4))
