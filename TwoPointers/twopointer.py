"""Coding Challenges"""

# Given an array of numbers sorted in ascending order and a target sum,
# find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers
# (i.e. the pair) such that they add up to the given target. If no such pair exists return [-1, -1].

# Example 1:

# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
# Example 2:

# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11


def find_target_sum(arr, target):
    """Find target sum"""
    left, right = 0, len(arr) - 1
    target_sum = 0
    while left < right:
        target_sum = arr[left] + arr[right]

        if target_sum == target:
            return [left, right]
        if target_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


print(find_target_sum([1, 2, 3, 4, 6], 6) == [1, 3])
print(find_target_sum([2, 5, 9, 11], 11) == [0, 2])

# Given an array of sorted numbers, move all non-duplicate number
# instances at the beginning of the array in-place. The non-duplicate
# numbers should be sorted and you should not
# use any extra space so that the solution has constant space complexity i.e., .

# Move all the unique number instances at the beginning of the array and after moving
# return the length of the subarray that has no duplicate in it.

# Example 1:

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after moving element will be [2, 3, 6, 9].
# Example 2:

# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after moving elements will be [2, 11].


def first_non_duplicate(arr):
    """first non duplicate"""
    first_non_duplicate_num = 1
    i = 0

    while i < len(arr):

        if arr[first_non_duplicate_num - 1] != arr[i]:
            arr[first_non_duplicate_num] = arr[i]

            first_non_duplicate_num += 1

        i += 1

    return first_non_duplicate_num


print(first_non_duplicate([2, 3, 3, 3, 6, 9, 9]) == 4)
print(first_non_duplicate([2, 2, 2, 11]) == 2)


# Problem Statement
# Given a sorted array, create a new array containing squares of all
# the numbers of the input array in the sorted order.

# Example 1:

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Example 2:

# Input: [-3, -1, 0, 1, 2]
# Output: [0, 1, 1, 4, 9]


def sort_array_by_power(arr):
    """Sorted array by power"""
    left_pointer, right_pointer, high_index = 0, len(arr) - 1, len(arr) - 1
    squares =list(range(len(arr)))
    while left_pointer <= right_pointer:
        left_square = arr[left_pointer] * arr[left_pointer]
        right_square = arr[right_pointer] * arr[right_pointer]

        if right_square > left_square:
            squares[high_index] = right_square
            right_pointer -= 1
        else:
            squares[high_index] = left_square
            left_pointer += 1
        high_index -= 1

    return squares


print(sort_array_by_power([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9])
print(sort_array_by_power([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9])
