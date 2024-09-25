#################################

# Prompt:

#################################

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # If the input is empty, return an empty list
        if not intervals:
            return []
        
        # Sort the intervals by their start time
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the result with the first interval
        result = [intervals[0]]
        
        # Iterate through the rest of the intervals
        for start, end in intervals[1:]:
            # Get the last interval in the result
            last_start, last_end = result[-1]
            
            # Check if the current interval overlaps with the last interval
            if start <= last_end:
                # Merge the current interval with the last interval
                result[-1] = [last_start, max(last_end, end)]
            else:
                # Add the current interval to the result
                result.append([start, end])
        
        return result


if __name__ == '__main__':
    test_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    for i in range(1_000):
        test_solution = Solution().merge(test_intervals)
