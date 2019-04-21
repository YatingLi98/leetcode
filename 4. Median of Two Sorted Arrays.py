class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l1, l2 = len(nums1), len(nums2)
        pos = (l1 + l2) // 2
        point1, point2 = 0, 0
        s = []
        while pos >= 0:
            if point1 < l1 and point2 < l2:
                if nums1[point1] < nums2[point2]:
                    s.append(nums1[point1])
                    point1 += 1
                else:
                    s.append(nums2[point2])
                    point2 += 1
            elif point1 == l1:
                s.append(nums2[point2])
                point2 += 1
            else:
                s.append(nums1[point1])
                point1 += 1
            pos -= 1
        if (l1 + l2) % 2 == 0:
            return (s[-1] + s[-2]) / 2.0
        return s[-1]


nums1 = [1, 3]
nums2 = [2]
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
