class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        c = nums1 + nums2
        c.sort()
        if(len(c) % 2 == 0):
            return (c[int((len(c)/2)) - 1] + c[int(len(c)/2)])/2
        return c[int(len(c)/2)]