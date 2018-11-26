'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums = {}
        for i in range(len(nums)):
            dict_nums[nums[i]] = i
            
        for j in range(len(nums)):
            res = target - nums[j]
            if dict_nums.get(res) is not None and dict_nums.get(res) != j:
                return [j, dict_nums.get(res)]

if __name__ == "__main__":
    nums = [3, 3]
    target = 6
    sol = Solution()
    print(sol.twoSum(nums, target))
        
