"""Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?"""


def fine_sum_of_two(num_arr, k):
    _num_arr = list(num_arr)  # O(n)
    _num_arr.sort()  # O(n log n)
    i = 0
    _num_arr_size = len(_num_arr) - 1  # O(n)
    while i != _num_arr_size:  # O(n)
        if _num_arr[i] + _num_arr[_num_arr_size] == k:
            return _num_arr[i], _num_arr[_num_arr_size]
        if _num_arr[i] + _num_arr[_num_arr_size] < k:
            i += 1
            continue
        if _num_arr[i] + _num_arr[_num_arr_size] > k:
            _num_arr_size -= 1
            continue
    return None


a = [10, 15, 3, 7]
k = 17

print(fine_sum_of_two(a, k))
