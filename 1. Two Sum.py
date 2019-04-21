class Solution:
    def twoSum(self, nums, target):
        dictionary = {}
        for i in range(len(nums)):
            dictionary[nums[i]] = i
        for i in range(len(nums)):
            need = target - nums[i]
            if need in dictionary and i != dictionary[need]:
                return [i, dictionary[need]]
