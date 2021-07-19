'''
You are given a sorted array in ascending order that is rotated at some unknown pivot (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]) and a target value.

Write a function that returns the target value's index. If the target value is not present in the array, return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


def findValueSortedShiftedArray(nums, target):
    
    if len(nums) == 0:
        return

    min = 0
    max = len(nums) - 1

    while min <= max:
        middle = (min + max) // 2

        if nums[middle] == target:
            return middle

        elif nums[middle] < target:
            min = middle + 1

        else:
            max = middle - 1

        if max < min:
            return nums[min]

    else:
        return -1

# O(log n)


# I was already capable of implementing binary searches in both their normal and rotated forms. However,
#  creating a shifted version of this algorithm was a tad perplexing during my first execution attempt.
#  Only after I reflected on how my code was executing did I realize that my max variable was being
# lowered to -1 by my else statement. That's when it became clear to me what 'shifting' entailed for
# this algorithm.

'''
Provide a summary of your solution to this challenge. Describe the process that you went through 
during your attempts to solve it. What specific obstacles or difficulties did you encounter in the 
process of solving it?
'''

# I was already capable of implementing binary searches in both their normal and rotated forms. However,
# creating a shifted version of this algorithm was a tad perplexing during my first execution attempt.
# Only after I reflected on how my code was executing did I realize that my max variable was being
# lowered to -1 by my else statement. That's when it became clear to me what 'shifting' entailed for
# this algorithm.

'''
Explain the time and space complexity of your solution. Is that the most efficient approach? If not, 
how could you improve the time and/or space complexity of your solution?
'''

# Considering a while loop was used with nested conditional statements, the algorithm I wrote must have
# a time/space complexity of O(log n).

# This is the only approach to solving this problem that I know of. Thankfully, it's also the most
# efficient.
