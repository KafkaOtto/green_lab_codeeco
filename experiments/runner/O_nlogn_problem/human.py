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
    test_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    for i in range(1_000_000):
        test_solution = Solution().merge(test_intervals)
