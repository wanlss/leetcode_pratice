"""
无重复字符的最长字串
使用滑动窗口的方法
滑动窗口都终点向字符串末尾移动，如果出现重复字符，则滑动窗口都起始位置一只向后移动，直到窗口内没有重复字符，再将终点向后移动
统计移动过程中出现的最长字符串
"""


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        counter = 0
        max_len = 0
        while end < len(s):  # 从第一个字符循环到最后一个字符
            if lookup[s[end]] > 0:  # 如果字典出现该字符的值大于0，说明该字符已经出现，因为出现过的字符值都为1
                counter += 1  # 出现重复字符，则计数加1
            lookup[s[end]] += 1  # 将每个字符作为键，初始值为1
            end += 1  # 滑动窗口都终点向后移动一位
            while counter > 0:  # 当出现重复字符都情况
                if lookup[s[start]] > 1:  #判断滑动窗口都第一个字符是不是重复字符
                    counter -= 1  # 如果是重复字符，则将计数减1
                lookup[s[start]] -= 1  # 将滑动窗口都起点对应字符都值减1(设置成初始值0)，防止下一次滑动窗口出现相同字符
                start += 1  # 将滑动窗口的起始位置向后移动，直到将重复字符移出窗口
            max_len = max(max_len, end - start)  # 再出现重复字符之前，end - start就是无重复字符的长度，出现重复字符之后，start的位置变成重复字符的下一个字符
        return max(max_len, end - start)  # 若最长无重复字符需要等到窗口移动到最后一个字符才出现，那么需要与之前的最长字符进行比较


if __name__ == '__main__':
    S = Solution()
    max_len = S.lengthOfLongestSubstring("abca")
    print(max_len)
