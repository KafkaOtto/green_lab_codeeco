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
        for current_interval in intervals[1:]:
            # Get the last interval in the result
            last_interval = result[-1]
            
            # Check if the current interval overlaps with the last interval
            if current_interval[0] <= last_interval[1]:
                # Merge the current interval with the last interval
                result[-1] = [last_interval[0], max(last_interval[1], current_interval[1])]
            else:
                # Add the current interval to the result
                result.append(current_interval)
        
        return result



if __name__ == '__main__':
    test_intervals = [[673, 687], [39, 785], [50, 114], [3, 40], [63, 282], [484, 556], [83, 84], [60, 97], [307, 433], [253, 276], [381, 454], [730, 809], [52, 77], [20, 24], [269, 493], [332, 454], [500, 511], [461, 483], [782, 830], [82, 302], [344, 586], [23, 67], [53, 255], [303, 532], [304, 414], [530, 613], [21, 210], [33, 68], [174, 386], [272, 299], [263, 390], [86, 305], [37, 247], [8, 11], [151, 158], [68, 73], [68, 114], [18, 100], [12, 837], [146, 518], [393, 424], [25, 134], [439, 527], [169, 326], [408, 428], [235, 474], [46, 532], [723, 756], [506, 511], [57, 137]]
    
    for i in range(800_000):
        test_solution = Solution().merge(test_intervals)
