class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        else:
            max_str = ''
            for i in range(len(s)):
                tmp_str2 = ''
                if i+1 < len(s) and s[i] == s[i+1]:
                    tmp_str2 = self.centerexpand(s,i-1,i+1+1)
                tmp_str1 = self.centerexpand(s,i-1,i+1)
                print(tmp_str1, tmp_str2, max_str)
                if len(tmp_str1) > len(tmp_str2):
                    tmp_str = tmp_str1
                else: tmp_str = tmp_str2
                if len(tmp_str) > len(max_str):
                        max_str = tmp_str
            return max_str

    def centerexpand(self,s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
if __name__ == "__main__":
    sol = Solution()
    s = "SQQSYYSQQS"
    print(sol.longestPalindrome(s))