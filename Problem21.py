"""Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2."""


def sol(arr):
    _arr = sorted(arr, key=lambda x: x[0])
    classes = []
    while len(_arr):
        current_class = [_arr.pop(0)]
        classes.append(current_class)
        for lecture in _arr:
            if lecture[0] > (current_class[len(current_class) - 1])[1]:
                current_class.append(lecture)
                _arr.remove(lecture)
    return len(classes)


a = [(30, 75), (0, 50), (60, 150)]
print(sol(a))
