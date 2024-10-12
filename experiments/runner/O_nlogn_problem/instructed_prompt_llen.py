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
    # import time

    # s_t = time.process_time()

    intervals = []
    with open('arr1.txt', 'r') as f:
        for line in f:
            start, end = map(int, line.split())
            intervals.append([start, end])

    # print('Read time: ', time.process_time() - s_t)

    for i in range(42_000):
        test_solution = Solution().merge(intervals)

    # print('Read time: ', time.process_time() - s_t)
