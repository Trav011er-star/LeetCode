# 超时，每次都要重新构造一个列表
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        c_list = sorted([c for c in p])
        c_set = set(c_list)
        result = []
        left = 0
        while left <= (len(s) - len(p)):
            if s[left] in c_set:
                sub_list = sorted([s[left + right] for right in range(len(c_list))])
                if c_list == sub_list:
                    result.append(left)
            left += 1
        return result


# 正确做法：移动固定窗口，每次不用构造新的列表，只要修改字符数量的统计值
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []

        window_count = [0] * 26
        p_count = [0] * 26
        result = []
        # 统计 p 和第一个窗口的字符
        for i in range(len(p)):
            p_count[ord(p[i]) - ord("a")] += 1
            window_count[ord(s[i]) - ord("a")] += 1

        # 移动固定大小的窗口
        for i in range(len(s) - len(p) + 1):
            if window_count == p_count:
                result.append(i)

            if i < len(s) - len(p):
                window_count[ord(s[i]) - ord("a")] -= 1
                window_count[ord(s[i + len(p)]) - ord("a")] += 1

        return result
