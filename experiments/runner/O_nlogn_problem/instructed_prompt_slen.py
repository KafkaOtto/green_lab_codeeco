#################################

# Prompt:

#################################

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals by their start time
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the result with the first interval
        result = [intervals[0]]
        
        # Iterate through the rest of the intervals
        for current_interval in intervals[1:]:
            # Get the last interval in the result
            last_interval = result[-1]
            
            # Check if the current interval overlaps with the last interval
            if current_interval[0] <= last_interval[1]:
                # Merge the current interval with the last interval
                last_interval[1] = max(last_interval[1], current_interval[1])
            else:
                # Add the current interval to the result
                result.append(current_interval)
        
        return result


if __name__ == '__main__':
    test_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    for i in range(1_000_000):
        test_solution = Solution().merge(test_intervals)
