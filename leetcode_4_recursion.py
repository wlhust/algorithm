class Solution(object):
    def __init__(self):
        self.count = 0
        self.flag_2 = 0
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if self.flag_2 == 0:
            self.end_len = (len(nums1) + len(nums2) +1 ) / 2
        self.flag_2 += 1
        if nums1 == []:
            flag = -1
        elif nums2 == []:
            flag = 1
        elif nums1 == [] and nums2 == []:
            return None
        elif nums2[0] > nums1[0]:
            flag = 1
        else:
            flag = -1

        if flag >= 0:
            self.count += 1
            if self.end_len*2 % 2 != 0:
                if self.count == int(self.end_len-0.5):
                    if nums2 != []:    
                        if (len(nums1) > 1 and nums1[1] > nums2[0]) or len(nums1) == 1:
                            return (nums1[0] + nums2[0]) / 2
                        else:
                            return (nums1[0] + nums1[1]) / 2    
                    else:
                        return (nums1[0] + nums1[1]) / 2
                else:
                    nums1.pop(0)
                    return self.findMedianSortedArrays(nums1,nums2)
            else:
                if self.count == int(self.end_len):
                    return nums1[0]
                else:
                    nums1.pop(0)
                    return self.findMedianSortedArrays(nums1,nums2)

        else:
            self.count += 1
            if self.end_len*2 % 2 != 0:
                if self.count == int(self.end_len-0.5):
                    print(nums1)
                    print(nums2)
                    if nums1 != []: 
                        if (len(nums2) > 1 and nums2[1] > nums1[0]) or len(nums2) == 1:
                            return (nums2[0] + nums1[0]) / 2
                        else:
                            return (nums2[0] + nums2[1]) / 2
                    else:
                        return (nums2[0] + nums2[1]) / 2
                else:
                    nums2.pop(0)
                    return self.findMedianSortedArrays(nums1,nums2)
            else:    
                if self.count == int(self.end_len):
                    return nums2[0]
                else:
                    nums2.pop(0)
                    return self.findMedianSortedArrays(nums1,nums2)
