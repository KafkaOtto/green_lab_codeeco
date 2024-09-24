#################################

# Problems: see report
# The time complexity is O(n⋅k+m⋅k) where (n) is the length of arr1, (m) is the length of arr2,
#                   and (k) is the average number of digits in the integers.
# space complexity: The space complexity is O(n⋅k) due to storing prefixes in the hashmap.

# links to solution:https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/solutions/5825830/step-by-step-guide-to-cracking-the-longest-common-prefix
#################################


from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_map = {}

        # Step 1: Build the prefix map for arr1
        for num in arr1:
            str_num = str(num)
            prefix = ""
            for ch in str_num:
                prefix += ch
                prefix_map[prefix] = prefix_map.get(prefix, 0) + 1

        max_length = 0

        # Step 2: Check for common prefixes in arr2
        for num in arr2:
            str_num = str(num)
            prefix = ""
            for ch in str_num:
                prefix += ch
                if prefix in prefix_map:
                    max_length = max(max_length, len(prefix))

        return max_length


if __name__ == '__main__':
    arr1 = [93, 93923, 786, 986]
    arr2 = [9392, 939321, 9392356]

    max_length = Solution().longestCommonPrefix(arr1, arr2)
    print(max_length)