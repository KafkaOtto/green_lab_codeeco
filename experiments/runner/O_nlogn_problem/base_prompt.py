
#################################

# Prompt: please give me the python solution for the following question: question

#################################

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for current_interval in intervals[1:]:
            # Get the last merged interval
            last_merged_interval = merged[-1]

            # Check if the current interval overlaps with the last merged interval
            if current_interval[0] <= last_merged_interval[1]:
                # Merge the current interval with the last merged interval
                merged[-1] = [last_merged_interval[0], max(last_merged_interval[1], current_interval[1])]
            else:
                # Add the current interval to the list of merged intervals
                merged.append(current_interval)

        return merged

if __name__ == '__main__':
    # import time

    # s_t = time.process_time()

    intervals = []
    with open('./experiments/runner/O_nlogn_problem/arr1.txt', 'r') as f:
        for line in f:
            start, end = map(int, line.split())
            intervals.append([start, end])

    # print('Read time: ', time.process_time() - s_t)

    for i in range(42_000):
        test_solution = Solution().merge(intervals)

    # print('Read time: ', time.process_time() - s_t)
