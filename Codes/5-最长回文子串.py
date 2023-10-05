'''
Date: 2023-10-05 22:27
Author: Sijia Lu
LastEditors: Sijia Lu
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Step 1: 判断是否为回文串
        Step 2: 判断是否为最长回文串
        '''
        if len(s) == 1:
            return s
        
        def isPalindrome(s):
            if s == s[::-1]:
                return True
            else:
                return False
        
        max_len = 0
        max_str = ''
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if isPalindrome(s[i:j]) and len(s[i:j]) > max_len:
                    max_len = len(s[i:j])
                    max_str = s[i:j]
        return max_str

# 优化 - 动态规划

