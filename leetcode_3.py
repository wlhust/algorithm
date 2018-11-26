'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    num =0 
    a = ''
    max_num = 0
    for i in s:
        if i in a:
            idx = a.index(i)
            a = a[idx+1:] + i
            num = len(a)
        else:
            num += 1
            a = a + i
            if num > max_num:
                max_num = num
    return max_num

if __name__ == "__main__":
    print(lengthOfLongestSubstring("pwwkew"))
