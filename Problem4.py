"""Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""


def sol(arr):
    max_val = 0
    for val in arr:  # O(n)
        if val > max_val:
            max_val = val
    index_arr = (max_val + 1) * [0]  # O(k) space complexity
    for num in arr:  # O(n)
        if num >= 0:
            index_arr[num] = 1
    for i in range(1, max_val + 1):  # O(n)
        if index_arr[i] == 0:
            return i
    return max_val + 1


a = [3, 4, -1, 1]
print(sol(a))
a = [1, 2, 0]
print(sol(a))
