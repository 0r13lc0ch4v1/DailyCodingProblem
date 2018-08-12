"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_unival_subtrees_helper(subroot):
    if not subroot:
        return 0, None

    count, unival_left = count_unival_subtrees_helper(subroot.left)
    _count, unival_right = count_unival_subtrees_helper(subroot.right)
    count += _count
    if subroot.left is None and subroot.right is None:
        return count + 1, subroot.val

    if not (subroot.left and subroot.right):
        if unival_left == subroot.val or subroot.val == unival_right:
            return count + 1, subroot.val
        else:
            return count, None

    if unival_left == subroot.val == unival_right:
        return count + 1, subroot.val

    return count, None


def count_unival_subtrees(root):
    return count_unival_subtrees_helper(root)[0]


tree = """   
   0
  / \\
 1   0
    / \\
   1   0
  / \\
 1   1"""

_root = Node(val=0, left=Node(val=1),
             right=Node(val=0, left=Node(val=1, left=Node(val=1), right=Node(val=1)), right=Node(val=0)))
print(tree, '\nNum of unival subtrees: ' + str(count_unival_subtrees(_root)))

tree = """   
   0
  / \\
 1   0
    / \\
   0   0
  / \\
 1   1"""
_root = Node(val=0, left=Node(val=1),
             right=Node(val=0, left=Node(val=0, left=Node(val=1), right=Node(val=1)), right=Node(val=0)))
print(tree, '\nNum of unival subtrees: ' + str(count_unival_subtrees(_root)))

tree = """   
   1
  / \\
 1   1
    / \\
   1   1
  / \\
 1   1"""
_root = Node(val=1,left=Node(val=1),
             right=Node(val=1, left=Node(val=1, left=Node(val=1), right=Node(val=1)), right=Node(val=1)))
print(tree, '\nNum of unival subtrees: ' + str(count_unival_subtrees(_root)))

tree = """   
   1
    \\
     1
    / \\
   1   1
  / \\
 1   1"""
_root = Node(val=1,
             right=Node(val=1, left=Node(val=1, left=Node(val=1), right=Node(val=1)), right=Node(val=1)))
print(tree, '\nNum of unival subtrees: ' + str(count_unival_subtrees(_root)))
