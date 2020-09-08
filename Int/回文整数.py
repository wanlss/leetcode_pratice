"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y, res = abs(x), 0
        while y != 0:
            res = res * 10 + y % 10
            y //= 10
        if res == x:
            return True
        return False


if __name__ == '__main__':
    S = Solution()
    print(S.isPalindrome(1221))