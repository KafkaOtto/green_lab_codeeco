#################################

# Prompt: please give me the python solution for the following question: question

#################################

from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def common_prefix(x, y):
            x, y = str(x), str(y)
            length = min(len(x), len(y))
            for i in range(length):
                if x[i]!= y[i]:
                    return i
            return length

        max_prefix = 0
        for x in arr1:
            for y in arr2:
                prefix = common_prefix(x, y)
                max_prefix = max(max_prefix, prefix)

        return max_prefix

if __name__ == '__main__':
    arr1 = [42, 47, 1, 26, 34, 12, 13, 46, 6, 16, 10, 49, 8, 24, 35, 2, 17, 21, 39, 41, 14, 32, 29, 25, 27, 45, 20, 9, 3, 36, 28, 33, 7, 43, 11, 5, 38, 30, 37, 50, 19, 18, 40, 22, 15, 23, 31, 44, 4, 48]
    arr2 = [1, 26, 34, 12, 13, 46, 6, 16, 10, 49, 8, 24, 35, 2, 17, 21, 39, 41, 14, 32, 29, 25, 27, 45, 20, 9, 3, 36, 28, 33, 7, 43, 11, 5, 38, 30, 37, 50, 19, 18, 40, 22, 15, 23, 31, 44, 4, 48, 84, 67]
    for i in range(800_000):
        max_length = Solution().longestCommonPrefix(arr1, arr2)
