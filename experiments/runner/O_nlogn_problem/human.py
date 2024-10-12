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
