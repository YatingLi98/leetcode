class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        pointer1 = 0
        pointer2 = 1
        while pointer2 < len(nums):
            if nums[pointer2] != nums[pointer1]:
                pointer1 += 1
                nums[pointer1] = nums[pointer2]
            pointer2 += 1

        return pointer1 + 1


s = Solution()
nums = [0, 0, 1, 2, 2, 2, 3]
print(s.removeDuplicates(nums))
print(nums)

"""
class Solution:
    def removeDuplicates(self, nums):
        index = 1
        while index < len(nums):
            if nums[index] == nums[index - 1]:
                nums.pop(index)
            else:
                index += 1
        return len(nums)
"""

"""
class Solution:
    def removeDuplicates(self, nums):
        nums = self.check_first(nums[0], nums[1:])
        print(nums)
        return len(nums)

    def check_first(self, x, nums):
        if len(nums) == 1:
            if x == nums[0]:
                return [x]
            else:
                return [x] + nums
        if x == nums[0]:
            return self.check_first(x, nums[1:])
        else:
            return [x] + self.check_first(nums[0], nums[1:])

"""
