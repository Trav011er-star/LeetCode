class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # 统计目标字符串中每个字符需要的数量
        dict_goal = {}

        for c in t:
            if c in dict_goal:
                dict_goal[c] += 1
            else:
                dict_goal[c] = 1

        # 当前窗口中目标字符的数量
        dict_window = {key: 0 for key in dict_goal}

        left = 0
        valid = 0

        min_start = 0
        min_length = len(s) + 1

        # right 不断扩大窗口
        for right in range(len(s)):
            right_char = s[right]

            # 将右边字符加入窗口
            if right_char in dict_goal:
                dict_window[right_char] += 1

                # 这个字符的数量刚好达到要求
                if dict_window[right_char] == dict_goal[right_char]:
                    valid += 1

            # 当前窗口满足要求，尝试从左边收缩
            while valid == len(dict_goal):
                current_length = right - left + 1

                # 记录更短的窗口
                if current_length < min_length:
                    min_length = current_length
                    min_start = left

                left_char = s[left]

                # 将左边字符移出窗口
                if left_char in dict_goal:
                    # 移出前刚好满足，移出后就不满足了
                    if dict_window[left_char] == dict_goal[left_char]:
                        valid -= 1

                    dict_window[left_char] -= 1

                left += 1

        if min_length == len(s) + 1:
            return ""

        return s[min_start : min_start + min_length]


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    solution = Solution()
    print(solution.minWindow(s, t))
