"""
回文字符串，正着和倒着的顺序一样
1. 暴力便利法
2. 中心扩散法
3. 动态规划
"""


class Solution:

    def longestPalindrome(self, s: str) -> str:
        """
        暴力破解法
        :param s:
        :return:
        """
        max_len = 0
        max_sub_str = ""
        s_length = len(s)
        for i in range(s_length):
            for j in (i, s_length):
                sub_s = s[i: j + 1]
                if sub_s == sub_s[::-1] and len(sub_s) > max_len:
                    max_sub_str = sub_s
                    max_len = len(sub_s)
        return max_sub_str

    def longestPalindrome_centerSpread(self, s: str) -> str:
        """
        中心扩散法
        :param s:
        :return:
        """
        size = len(s)
        if size < 2:
            return s

        max_len = 1
        res = s[0]
        for i in range(size):
            # 当字符串长度为奇数
            palindrome_odd, palindrome_odd_len = self.__center_spread(s, size, i, i)
            # 当字符串长度为偶数
            palindrome_even, palindrome_even_len = self.__center_spread(s, size, i, i + 1)
            curr_max_sub = palindrome_odd if palindrome_odd_len > palindrome_even_len else palindrome_even
            if len(curr_max_sub) > max_len:
                max_len = len(curr_max_sub)
                res = curr_max_sub
        return res

    def __center_spread(self, s, size, l, r):
        left = l
        right = r
        while left >= 0 and right < size and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right], right - left + 1



if __name__ == '__main__':
    # S = Solution()
    # print(S.longestPalindrome_centerSpread("abcb"))
    x = input()
    print(x, type(x))
    a = float(x)
    print(a)
