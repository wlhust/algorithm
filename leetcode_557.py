class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        s_new = ''
        for i in range(len(words)):
            s_new += ' '+ words[i][::-1]
        return s_new.strip()