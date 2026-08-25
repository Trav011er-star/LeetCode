class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 提示：滑动窗口
        max_len = 0
        left = 0
        c_set = set()

        # 左指针负责删除，保证窗口 [left, right] 内没有重复的字符
        for right in range(len(s)):
            # 当前字符已经存在时，不断缩小左边界
            while s[right] in c_set:
                c_set.remove(s[left])
                left += 1

            # 将当前字符加入窗口
            c_set.add(s[right])

            # 当前窗口为 [left, right]
            current_len = right - left + 1
            max_len = max(max_len, current_len)

        return max_len
