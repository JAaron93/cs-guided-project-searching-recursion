'''
Which logarithmic expression is identical to the following exponential expression?
2^n = 64
'''

# Answer:
# log_2 64 = n

'''
When trying to solve an algorithmic coding challenge, what keywords should you look out for that might alert you that logarithms are involved?
'''

# Answers:
# double, divide in half, binary search, the height of a tree

'''
What type of search algorithm is used in this representation?
'''

# Answer:
# Binary Search

'''
Below is an example implementation of the binary search algorithm in Python:
'''


def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    while first <= last:
        mid = first + (last - first) // 2
        if item_list[mid] == item:
            return True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


'''
What must be true for this algorithm to work?
'''

# Answer:
# 'item_list' must be sorted from smallest to greatest
