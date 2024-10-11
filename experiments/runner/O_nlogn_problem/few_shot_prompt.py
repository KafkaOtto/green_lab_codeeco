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
    test_intervals = [[673, 687], [39, 785], [50, 114], [3, 40], [63, 282], [484, 556], [83, 84], [60, 97], [307, 433], [253, 276], [381, 454], [730, 809], [52, 77], [20, 24], [269, 493], [332, 454], [500, 511], [461, 483], [782, 830], [82, 302], [344, 586], [23, 67], [53, 255], [303, 532], [304, 414], [530, 613], [21, 210], [33, 68], [174, 386], [272, 299], [263, 390], [86, 305], [37, 247], [8, 11], [151, 158], [68, 73], [68, 114], [18, 100], [12, 837], [146, 518], [393, 424], [25, 134], [439, 527], [169, 326], [408, 428], [235, 474], [46, 532], [723, 756], [506, 511], [57, 137]]

    for i in range(800_000):
        test_solution = Solution().merge(test_intervals)
