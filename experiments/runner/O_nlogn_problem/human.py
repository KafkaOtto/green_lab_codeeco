#################################

# Problems: Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# average time complexity: O(nlogn)
# space complexity O(n)

# links to solution: https://leetcode.com/problems/merge-intervals/solutions/5649346/easiest-python-solution-using-lambda
#################################

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        result = [intervals[0]]
        c = 0
        for x in intervals[1:]:
            if result[c][1] >= x[0]:
                if result[c][1] < x[1]:
                    result[c][1] = x[1]
            else:
                result.append(x)
                c += 1

        return result


if __name__ == '__main__':
    test_intervals = [[673, 687], [39, 785], [50, 114], [3, 40], [63, 282], [484, 556], [83, 84], [60, 97], [307, 433], [253, 276], [381, 454], [730, 809], [52, 77], [20, 24], [269, 493], [332, 454], [500, 511], [461, 483], [782, 830], [82, 302], [344, 586], [23, 67], [53, 255], [303, 532], [304, 414], [530, 613], [21, 210], [33, 68], [174, 386], [272, 299], [263, 390], [86, 305], [37, 247], [8, 11], [151, 158], [68, 73], [68, 114], [18, 100], [12, 837], [146, 518], [393, 424], [25, 134], [439, 527], [169, 326], [408, 428], [235, 474], [46, 532], [723, 756], [506, 511], [57, 137]]
    for i in range(800_000):
        test_solution = Solution().merge(test_intervals)
