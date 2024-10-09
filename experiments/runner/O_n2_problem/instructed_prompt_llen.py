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
    arr1 = [93, 93923, 786, 986]
    arr2 = [9392, 939321, 9392356]
    for i in range(25_000_000):
        max_length = Solution().longestCommonPrefix(arr1, arr2)
