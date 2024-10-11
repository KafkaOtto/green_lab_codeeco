#################################

# Instucted Prompt

#################################



from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Convert all integers to strings
        arr1 = [str(num) for num in arr1]
        arr2 = [str(num) for num in arr2]
        
        # Initialize the maximum common prefix length to 0
        max_common_prefix_length = 0
        
        # Iterate over all pairs of strings from arr1 and arr2
        for str1 in arr1:
            for str2 in arr2:
                # Initialize the common prefix length to 0
                common_prefix_length = 0
                
                # Find the common prefix length between str1 and str2
                for i in range(min(len(str1), len(str2))):
                    if str1[i] == str2[i]:
                        common_prefix_length += 1
                    else:
                        break
                
                # Update the maximum common prefix length
                max_common_prefix_length = max(max_common_prefix_length, common_prefix_length)
        
        return max_common_prefix_length


if __name__ == '__main__':
    arr1 = [42, 47, 1, 26, 34, 12, 13, 46, 6, 16, 10, 49, 8, 24, 35, 2, 17, 21, 39, 41, 14, 32, 29, 25, 27, 45, 20, 9, 3, 36, 28, 33, 7, 43, 11, 5, 38, 30, 37, 50, 19, 18, 40, 22, 15, 23, 31, 44, 4, 48]
    arr2 = [1, 26, 34, 12, 13, 46, 6, 16, 10, 49, 8, 24, 35, 2, 17, 21, 39, 41, 14, 32, 29, 25, 27, 45, 20, 9, 3, 36, 28, 33, 7, 43, 11, 5, 38, 30, 37, 50, 19, 18, 40, 22, 15, 23, 31, 44, 4, 48, 84, 67]

    for i in range(800_000):
        max_length = Solution().longestCommonPrefix(arr1, arr2)
