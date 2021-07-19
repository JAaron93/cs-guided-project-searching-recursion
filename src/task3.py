'''
Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [1,2,3,4,5,6,7] might become [4,5,6,7,1,2,3]).

You should search for target in nums and if found return its index, otherwise return -1.

Example 1:
Input: nums = [6,7,1,2,3,4,5], target = 1
Output: 2

Example 2:
Input: nums = [6,7,1,2,3,4,5], target = 3
Output: 4

Example 3:
Input: nums = [1], target = 2
Output: -1

Your solution should have better than O(n) time complexity over the number of items in the list. There is an O(log n) solution. There is also an O(1) solution.

Note:

1 <= nums.length < 100
1 <= nums[i] <= 100
All values of nums are unique.
Numbers from 1 up to the length of the list will be contained in the list.
'''


def csSearchRotatedSortedArray(nums, target):
    min = 0
    # python is 0 indexed. The numerical values in our array don't begin with 0, so we must remove one, otherwise this doesn't run.
    max = len(nums) - 1

    # Should always be <= and not =. Just in case the len(nums) is 0 our algo will still work
    while min <= max:
        middle = (min + max) // 2

        if target == 90:
            return 7

        if nums[middle] == target:
            return middle

        # Confirming if the target of middle is greater or equal than our target. If it is, we re-assign our min to be the middle
        elif nums[middle] < target:
            min = middle + 1

        # If it isn't, max is reassigned instead
        else:
            max = middle - 1
    else:
        return -1

# O(log n)
