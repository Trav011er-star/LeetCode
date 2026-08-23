# LeeCode 学习记录

本仓库用于记录我的 LeetCode 刷题过程，主要使用 Python 完成。

学习过程中不仅保存最终代码，还会整理每道题的解题思路、涉及的 Python 语法、代码执行过程，以及时间复杂度和空间复杂度。

## 学习目标

- 熟悉 Python 的常用语法和数据结构
- 掌握数组、字符串、列表和哈希表等基础知识
- 学会把题目条件转换为可以编程实现的解题思路
- 学习分析算法的时间复杂度和空间复杂度
- 记录错误思路、修改过程以及可以复用的解题方法

## 开发环境

- Python
- Visual Studio Code
- LeetCode

## 题目记录

| LeetCode 编号 | 题目 | 难度 | 主要知识点 | 时间复杂度 | 空间复杂度 |
| ---: | --- | --- | --- | --- | --- |
| 1 | 两数之和 | 简单 | 数组、哈希表、`enumerate()` | $O(n)$ | $O(n)$ |
| 49 | 字母异位词分组 | 中等 | 字符串排序、哈希表、列表 | $O(nk\log k)$ | $O(nk)$ |

其中，$n$ 表示字符串的数量，$k$ 表示字符串的最大长度。

---

## 1. 两数之和

### 题目描述

给定一个整数数组 `nums` 和一个整数目标值 `target`，在数组中找出和为 `target` 的两个整数，并返回它们在原数组中的下标。

每种输入只会对应一个答案，并且不能重复使用同一个元素。答案可以按任意顺序返回。

### 示例

```text
输入：nums = [2, 7, 11, 15], target = 9
输出：[0, 1]
解释：nums[0] + nums[1] = 2 + 7 = 9
```

### 解题思路

遍历数组时，对于当前数字 `num`，计算还需要寻找的数字：

```python
need = target - num
```

然后使用字典检查 `need` 是否在前面出现过。

字典中保存的内容为：

```text
数组中的数字 -> 该数字对应的下标
```

如果 `need` 已经在字典中，就说明找到了两个数：

```text
need + num = target
```

此时返回 `need` 的下标和当前数字的下标。

### Python 代码

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 创建哈希表：键保存数字，值保存数字对应的下标
        num_index = {}

        # enumerate() 可以同时获得元素的下标和值
        for i, num in enumerate(nums):
            # 计算当前还需要寻找的数字
            need = target - num

            # 对字典使用 in，判断的是对应的键是否存在
            if need in num_index:
                return [num_index[need], i]

            # 当前没有找到答案，保存当前数字和下标
            num_index[num] = i
```

### 执行过程

对于：

```python
nums = [2, 7, 11, 15]
target = 9
```

程序的执行过程如下：

| 当前下标 `i` | 当前数字 `num` | 需要的数字 `need` | 查找前的字典 | 操作 |
| ---: | ---: | ---: | --- | --- |
| 0 | 2 | 7 | `{}` | 没有找到 `7`，保存 `2: 0` |
| 1 | 7 | 2 | `{2: 0}` | 找到 `2`，返回 `[0, 1]` |

### 相关 Python 语法

#### 字典

字典可以作为哈希表使用，按照“键—值”的形式保存数据：

```python
num_index = {}
num_index[2] = 0
```

此时字典为：

```python
{2: 0}
```

其中 `2` 是键，`0` 是值，表示数字 `2` 在数组中的下标是 `0`。

#### `enumerate()`

`enumerate` 的含义是“枚举、逐个列举并编号”。它可以在遍历列表时，同时提供元素的下标和值：

```python
nums = [2, 7, 11]

for i, num in enumerate(nums):
    print(i, num)
```

输出：

```text
0 2
1 7
2 11
```

其中：

- `i` 是当前元素的下标
- `num` 是当前元素的值

#### `in`

对于字典：

```python
if need in num_index:
```

表示判断 `need` 是否存在于字典的键中，而不是判断它是否存在于字典的值中。

#### `return`

```python
return [num_index[need], i]
```

表示返回由两个下标组成的列表，并立即结束当前方法。

### 为什么先查找再保存

代码先执行：

```python
if need in num_index:
```

再执行：

```python
num_index[num] = i
```

这样可以避免把当前元素和它自己配对，从而满足“不能重复使用同一个元素”的要求。

例如：

```python
nums = [3, 3]
target = 6
```

第一次遍历时保存 `{3: 0}`，第二次遍历到另一个 `3` 时，才会找到之前保存的下标 `0`，最终返回 `[0, 1]`。

### 为什么不直接排序

如果直接执行：

```python
nums_order = sorted(nums)
```

数组中元素的位置可能发生变化，而题目要求返回元素在原数组中的下标。因此，如果使用排序法，还需要额外保存每个元素原来的位置。

对于本题，使用哈希表可以在不改变原数组顺序的情况下直接保存原始下标，代码也更加简洁。

### 复杂度分析

- 时间复杂度：$O(n)$。最坏情况下需要遍历整个数组一次。
- 空间复杂度：$O(n)$。最坏情况下需要把数组中的元素及其下标保存到字典中。

### 学习总结

这道题的核心不是直接寻找两个数，而是在遍历到当前数字时，快速判断它所需要的另一个数字是否已经出现。

哈希表利用额外的存储空间，将查找一个数字的平均时间复杂度从 $O(n)$ 降低到 $O(1)$，从而把整体时间复杂度从双重循环的 $O(n^2)$ 优化为 $O(n)$。

---

## 49. 字母异位词分组

### 题目描述

给定一个字符串数组 `strs`，将其中的字母异位词组合在一起，并按任意顺序返回分组结果。

字母异位词由相同的字母组成，并且每个字母出现的次数也相同，只是字母的排列顺序可能不同。

例如：

```text
eat、tea、ate
```

这三个单词都由一个 `a`、一个 `e` 和一个 `t` 组成，因此它们互为字母异位词。

### 示例

```text
输入：strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出：[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

题目允许按任意顺序返回结果，因此每个分组的顺序和不同分组之间的顺序都不需要与示例完全相同。

### 解题思路

字母异位词的字母排列顺序虽然不同，但是将每个单词中的字符排序后，它们会得到相同的结果：

```text
eat -> aet
tea -> aet
ate -> aet

tan -> ant
nat -> ant

bat -> abt
```

因此，可以把排序后的字符串作为字典的键，把原始字符串保存到这个键对应的列表中。

字典中保存的关系为：

```text
排序后的字符串 -> 具有相同字母组成的原字符串列表
```

最终字典类似于：

```python
{
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}
```

最后取出字典中的所有值，就可以得到题目要求的分组结果。

### Python 代码

```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        c_dict = {}

        for word in strs:
            # sorted()：按照字母顺序排列单词，返回一个字符列表
            # join()：将字符列表中的字符拼接起来，返回一个字符串
            symbol = "".join(sorted(word))

            if symbol in c_dict:
                c_dict[symbol].append(word)
            else:
                c_dict[symbol] = [word]

        # 遍历字典时，默认遍历字典的键
        return [c_dict[symbol] for symbol in c_dict]
```

代码中使用 `word` 作为变量名，而没有使用 `str`，因为 `str` 是 Python 内置的字符串类型名称。使用 `str` 作为普通变量虽然通常仍能运行，但会暂时覆盖内置名称。

### 执行过程

对于：

```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

程序的执行过程如下：

| 当前字符串 `word` | 排序结果 `symbol` | 操作后的字典 |
| --- | --- | --- |
| `"eat"` | `"aet"` | `{"aet": ["eat"]}` |
| `"tea"` | `"aet"` | `{"aet": ["eat", "tea"]}` |
| `"tan"` | `"ant"` | `{"aet": ["eat", "tea"], "ant": ["tan"]}` |
| `"ate"` | `"aet"` | `{"aet": ["eat", "tea", "ate"], "ant": ["tan"]}` |
| `"nat"` | `"ant"` | `{"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}` |
| `"bat"` | `"abt"` | 新建键 `"abt"`，并保存 `"bat"` |

### 相关 Python 语法

#### `sorted()`

`sorted()` 是 Python 的内置函数，可以对字符串中的字符进行排序：

```python
sorted("tea")
```

返回：

```python
['a', 'e', 't']
```

需要注意，`sorted()` 返回的是一个新列表，并不会直接返回字符串。

#### `join()`

`join()` 是字符串的方法，用于把多个字符串连接起来：

```python
"".join(['a', 'e', 't'])
```

返回：

```python
"aet"
```

其中前面的 `""` 表示使用空字符串作为连接符，也就是直接连接所有字符，中间不添加其他内容。

将两者组合起来：

```python
symbol = "".join(sorted(word))
```

执行顺序为：

1. `sorted(word)` 将字符串中的字符排序，得到字符列表；
2. `"".join(...)` 将字符列表重新拼接成字符串；
3. 将得到的字符串保存到变量 `symbol` 中。

#### 创建字典

使用一对花括号可以创建空字典：

```python
c_dict = {}
```

向字典中添加新的键值对：

```python
c_dict[symbol] = [word]
```

这里：

- `symbol` 是字典的键；
- `[word]` 是只包含当前字符串的列表，也是字典的值。

#### 字典中的 `in`

```python
if symbol in c_dict:
```

对于字典，`in` 默认判断的是某个对象是否存在于字典的键中，等价于：

```python
if symbol in c_dict.keys():
```

集合没有键和值。如果对集合使用 `in`，判断的是对象是否为集合中的元素。

#### `append()`

如果字典中已经存在当前键，说明之前已经遇到过同一类字母异位词：

```python
c_dict[symbol].append(word)
```

其中：

1. `c_dict[symbol]` 取得该键对应的列表；
2. `.append(word)` 将当前字符串添加到列表末尾。

例如：

```python
c_dict = {"aet": ["eat"]}
c_dict["aet"].append("tea")
```

结果为：

```python
{"aet": ["eat", "tea"]}
```

#### 列表推导式

```python
return [c_dict[symbol] for symbol in c_dict]
```

这是一条列表推导式，其含义是：

1. 遍历字典 `c_dict` 中的所有键；
2. 使用 `c_dict[symbol]` 取得每个键对应的值；
3. 将所有值组成一个新列表并返回。

它可以改写为普通循环：

```python
result = []

for symbol in c_dict:
    result.append(c_dict[symbol])

return result
```

也可以使用字典的 `values()` 方法简化为：

```python
return list(c_dict.values())
```

### 空字符串为什么也可以正确处理

当字符串为 `""` 时：

```python
sorted("")
```

得到空列表：

```python
[]
```

继续执行：

```python
"".join([])
```

得到空字符串 `""`。因此，空字符串可以正常作为字典的键：

```python
{"": [""]}
```

最终返回：

```python
[[""]]
```

### 复杂度分析

假设：

- `strs` 中有 $n$ 个字符串；
- 每个字符串的最大长度为 $k$。

对于每个字符串：

- 字符排序需要 $O(k\log k)$ 的时间；
- 拼接和保存字符串需要 $O(k)$ 的时间。

因此：

- 时间复杂度：$O(nk\log k)$；
- 空间复杂度：$O(nk)$，用于保存排序产生的内容和最终分组结果。

### 学习总结

这道题的关键是为每一组字母异位词寻找一个相同的“分类标志”。

将字符串排序后，所有互为字母异位词的字符串都会得到相同的结果，因此可以把排序结果作为字典的键。字典负责快速找到对应的分组，列表负责保存属于该分组的所有原字符串。

这是一种常见的哈希表分组思路：

```text
先为每个对象计算分类标志
            ↓
以分类标志作为字典的键
            ↓
把具有相同标志的对象保存到同一个列表
```

以后遇到“按照某种共同特征对元素进行分组”的题目时，也可以考虑使用这种方法。
