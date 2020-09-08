"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s  # 如果变换行数为一行，不用变换
        res = ["" for _ in range(numRows)]  # 初始化数组，每个元素表示变换后每一行到字符
        i, flag = 0, -1  # i表示循环到到行数，flag控制变换到方向
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:  # 如果字符轮到了第一行或者最后一行，则下个字符需要变换方向
                flag = -flag
            i += flag  # 变换行数
        return "".join(res)


if __name__ == '__main__':
    S = Solution()
    print(S.convert("LEETCODEISHIRING", 3))
