"""Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10,since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?"""


def find_max_sum(arr):
    incl = 0  # incl = Max sum including the previous element.
    excl = 0  # excl = Max sum excluding the previous element.

    for i in arr:
        new_excl = excl if excl > incl else incl

        incl = excl + i
        excl = new_excl

    return excl if excl > incl else incl


_arr = [5, 1, 1, 5]
print(find_max_sum(_arr))

_arr = [2, 4, 6, 2, 5]
print(find_max_sum(_arr))

_arr = [-1, 2, -13, 0, 1]
print(find_max_sum(_arr))
