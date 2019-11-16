class Solution:
    def multiply(self, num1, num2):
        ans = self.change_into_number(num1) * self.change_into_number(num2)
        return str(ans)


    def change_into_number(self, num):
        ans = 0
        if num[0] == '-':
            return -self.change_into_number(num[1:])
        index = 0
        while index < len(num):
            ans = ans * 10 + int(num[index])
            index += 1
        return ans




s = Solution()
str1 = "-122"
str2 = "123"
print(s.change_into_number(str1), s.change_into_number(str2))
