class Solution:
    nums = []
    target = None
    def searchRange(self, nums, target):
        self.nums = nums
        self.target = target
        if len(nums) == 0:
            return [-1, -1]
        low = self.search_low(0, len(self.nums)-1)
        high = self.search_high(low, len(self.nums)-1)
        return [low, high]

    def search_low(self, low, high):
        if low == high:
            if self.nums[low] == self.target:
                return low
            else:
                return -1
        medain = (low + high) // 2
        if self.nums[medain] < self.target:
            return self.search_low(medain+1, high)
        if self.nums[medain] >= self.target:
            return self.search_low(low, medain)

    def search_high(self, low, high):
        if low == high:
            if self.nums[low] == self.target:
                return low
            else:
                return -1
        medain = (low + high) // 2 + 1

        if self.nums[medain] <= self.target:
            return self.search_high(medain, high)
        if self.nums[medain] > self.target:
            return self.search_high(low, medain-1)





nums = [5,7,7,8,8,10]
target = 8
s = Solution()
#print(s.searchRange(nums, target))
import numpy as np
def construct_matrix(num_states, num_dices, num_sides):
    '''
    Arguments:
        num_states {int} -- number of the state
        num_dices {int} -- number of the dices
        num_sides {int} -- number of the sides each dice has

    Returns:
        P {numpy.array} -- n x n, transition matrix of the Markov chain
    '''
    P = np.zeros((num_states, num_states))
    possible_sum = [0]
    for i in range(num_dices):
        curr = []
        for ele in possible_sum:
            for a in range(1, num_sides + 1):
                curr.append(ele + a)
        possible_sum = curr
    return possible_sum


p = construct_matrix(2, 2, 4)
print(len(p))