"""
I was bored one day and decided to look at last names in the phonebook for my
area.

I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.

When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."

Example:

surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]

Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.

*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""


def find_rotation_point(surnames):
    # Your code here
    '''
    How do we find the rotation point?

    - Modified binary search
    '''
    if len(surnames) == 0:
        return
    # keep track of the first surname
    first_surname = surnames[0]
    # keep track of min
    min = 0
    # keep track of max
    max = len(surnames) - 1

    # while my min is less than my max
    while min < max:

        # create a guess at midpoint
        # guess = min + ((max - min) // 2)
        guess = min + max // 2

        # test if the surname at the index of guess is greater than or equal to the first surname
        if surnames[guess] >= first_surname:
            # set my min to the guess index
            min = guess
        # otherwise
        else:
            # set max to the guess index
            max = guess

        # check if the min + 1 is equal to the max:
        if min + 1 == max:
            # return the max to the caller
            return max


# testing
surnames = ['liu', 'mcdowell', 'nixon', 'sparks', 'zhang',
            'ahmed', 'brandt', 'davenport', 'farley', 'glover', 'kennedy']
print(find_rotation_point(surnames))
