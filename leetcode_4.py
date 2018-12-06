class Solution(object):
    def __init__(self):
        self.count = 0
        self.flag = 0
        self.sum = 0

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.end_len = (len(nums1) + len(nums2) +1 ) / 2
        if self.end_len * 2 % 2 == 0:
            self.flag = 1
        else:
            self.flag = -1

        for i in range(int(self.end_len) + 1):
            if nums1 == [] and nums2 == []:
                pass
            elif nums1 == [] and nums2 != []:
                pop = nums2.pop(0)
            elif nums2 == [] and nums1 != []:
                pop = nums1.pop(0)
            else:
                if nums1[0] > nums2[0]:
                    pop = nums2.pop(0)
                else:
                    pop = nums1.pop(0)
            if i == int(self.end_len) - 1:
                self.sum += pop
        if self.flag == 1:
            return self.sum
        else:
            print(self.sum)
            print(pop)
            return (self.sum + pop) / 2