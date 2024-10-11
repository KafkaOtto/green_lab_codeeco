#################################

# given three <question, answer>
# based on the examples, please give me answer solution for the question
#################################



from typing import List
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def common_prefix(a, b):
            prefix_len = 0
            while a and b:
                if a[0] == b[0]:
                    prefix_len += 1
                    a, b = a[1:], b[1:]
                else:
                    break
            return prefix_len

        max_len = 0
        for num1 in arr1:
            for num2 in arr2:
                prefix_len = common_prefix(str(num1), str(num2))
                max_len = max(max_len, prefix_len)

        return max_len

if __name__ == '__main__':
    arr1 = [42, 47, 1, 26, 34, 12, 13, 46, 6, 16, 10, 49, 8, 24, 35, 2, 17, 21, 39, 41, 14, 32, 29, 25, 27, 45, 20, 9, 3, 36, 28, 33, 7, 43, 11, 5, 38, 30, 37, 50, 19, 18, 40, 22, 15, 23, 31, 44, 4, 48]
    arr2 = [1, 26, 34, 12, 13, 46, 6, 16, 10, 49, 8, 24, 35, 2, 17, 21, 39, 41, 14, 32, 29, 25, 27, 45, 20, 9, 3, 36, 28, 33, 7, 43, 11, 5, 38, 30, 37, 50, 19, 18, 40, 22, 15, 23, 31, 44, 4, 48, 84, 67]

    for i in range(800_000):
        max_length = Solution().longestCommonPrefix(arr1, arr2)
