#################################

# given three <question, answer> given in the report
# based on the examples, please give me answer solution for the question
#################################

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            # If the current interval overlaps with the last merged interval, merge them
            if current[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], current[1])
            else:
                # Add the current interval to the list of merged intervals
                merged.append(current)

        return merged

if __name__ == '__main__':
    test_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    for i in range(25_000_000):
        test_solution = Solution().merge(test_intervals)
