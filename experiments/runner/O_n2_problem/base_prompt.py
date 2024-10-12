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
    # import time
    # start = time.process_time()

    with open('arr1.txt', 'r') as f:
        arr1 = [int(x) for x in f.read().split()]
    with open('arr2.txt', 'r') as f:
        arr2 = [int(x) for x in f.read().split()]

    # print('Time1: ', time.process_time() - start)

    max_length = Solution().longestCommonPrefix(arr1, arr2)

    # print('Time2: ', time.process_time() - start)