class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            l = len(nums)
            index = l - 1
            lst = [nums[index]]
            while index > 0:
                if nums[index - 1] >= nums[index]:
                    lst.append(nums[index - 1])
                    index -= 1
                else:
                    break
            if index == 0:
                nums.reverse()
            else:
                i = 0
                while i < len(lst):
                    if lst[i] > nums[index - 1]:
                        nums[index - 1], lst[i] = lst[i], nums[index - 1]
                        break
                    else:
                        i += 1
                j = 0
                while j < len(lst):
                    nums[index] = lst[j]
                    index += 1
                    j += 1


s = Solution()
nums = [1, 1, 5]
s.nextPermutation(nums)
print(nums)
