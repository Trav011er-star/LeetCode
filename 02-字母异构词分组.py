class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        c_dict = {}
        for str in strs:
            # sorted() : 按照字母顺序排列单词，返回一个字符列表
            # join() : 将字符列表的字符组合起来，返回一个字符串
            s = "".join(sorted(str))
            if s in c_dict:
                c_dict[s].append(str)
            else:
                c_dict[s] = [str]

        # 遍历一个字典，默认情况下是遍历字典的键
        return [c_dict[symbol] for symbol in c_dict]
