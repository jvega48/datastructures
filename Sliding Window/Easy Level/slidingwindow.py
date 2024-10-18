"""Easy - Coding Challenges - Sliding Window"""

# Given an array of positive numbers and a positive number 'k,'
# find the maximum sum of any contiguous subarray of size 'k'.

# Example 1:

# Input: arr = [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:

# Input: arr = [2, 3, 4, 1, 5], k=2
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].


import math


def find_maximum_sum_sub_array(array, k):
    """Find the maximum sum sub array"""

    if len(array) == 0:
        return 0

    results = current_window_sum = window_start = 0

    for window_end, value in enumerate(array):
        current_window_sum += value

        if window_end >= k - 1:
            results = max(current_window_sum, results)
            current_window_sum -= array[window_start]
            window_start += 1
    return results


def find_maximum_sum_sub_array_slow_way(array, k):
    """Find the maximum sum sub array slow way"""
    max_sum = window_sum = 0

    for i in range(len(array) - k + 1):
        window_sum = 0

        for j in range(i, i + k):
            window_sum += array[j]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Smallest Subarray With a Greater Sum (easy)
# Problem Statement
# Given an array of positive integers and a number ‘S,’ find the length of the
# smallest contiguous subarray whose sum is greater than or equal to 'S'.
# Return 0 if no such subarray exists.

# Example 1:

# Input: arr = [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
# Example 2:

# Input: arr = [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
# Example 3:

# Input: arr = [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than
# or equal to '8' are [3, 4, 1] or [1, 1, 6].
# Constraints:

# 1 <= S <=
# 1 <= arr.length <= 105
# 1 <= arr[i] <= 104


def find_min_sub_array(array, s):
    """Find the min sub array given a min number s"""
    min_length = math.inf
    window_start = window_sum = 0

    for window_end, value in enumerate(array):
        window_sum += value

        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= array[window_start]
            window_start += 1

    if min_length == math.inf:
        return 0
    return min_length
