"""Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?"""


# with division
def sol_one(arr):
    max_product = 1
    for num in arr:  # O(n)
        max_product *= num
    ans = []
    for num in arr:  # O(n)
        ans.append(max_product // num)
    return ans


a = [1, 2, 3, 4, 5]
print(sol_one(a))
a = [3, 2, 1]
print(sol_one(a))


# no division
def sol_two(arr):
    tmp = []
    for cell_val in arr:  # O(n) (for loop runtime complexity: O(n^2))
        _arr = list(arr)  # O(n)
        _arr.remove(cell_val)  # O(n)
        tmp.append(_arr)  # O(1)
    ans = len(arr) * [1]
    for index, lst in enumerate(tmp):  # O(n) (for loop runtime complexity: O(n^2))
        for num in lst:  # O(n)
            ans[index] *= num
    return ans


a = [1, 2, 3, 4, 5]
print(sol_two(a))
a = [3, 2, 1]
print(sol_two(a))
