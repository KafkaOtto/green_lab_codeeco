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
    arr1 = [93, 93923, 786, 986]
    arr2 = [9392, 939321, 9392356]
    for i in range(1_000):
        max_length = Solution().longestCommonPrefix(arr1, arr2)