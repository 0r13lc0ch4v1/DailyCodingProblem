"""Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed."""

letter_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                  'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                  'x': 24, 'y': 25, 'z': 26}


def decode_helper(msg, memo, counter):
    counter[0] += 1
    if not msg:
        return 1
    if memo[len(msg)]:
        return memo[len(msg)]
    if '0' == msg[0]:
        return 0
    if 1 == len(msg):
        return 1

    res = decode_helper(msg[1:], memo, counter)
    memo[len(msg)] = res
    if 1 <= int(str(msg[0]) + str(msg[1])) <= 26:
        res += decode_helper(msg[2:], memo, counter)
    return res


def decode(msg):
    counter = [0]
    memo = (len(msg) + 1) * [None]
    res = decode_helper(msg, memo, counter)
    return 'Result: {}.\nNumber of calls to get result: {}, string length: {}.'.format(res, counter, len(msg))


print(decode('111'))
print(decode('12121212'))
