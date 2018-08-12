"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'"""


def deserialize(s):
    NO_NODE_MARK = 'OC_Sol'
    tree_lst = s.split(',')

    def build_pre_order(nodes):
        if NO_NODE_MARK == nodes[0]:
            nodes.pop(0)
            return

        return Node(nodes.pop(0), build_pre_order(nodes), build_pre_order(nodes))

    return build_pre_order(tree_lst)


def serialize(root):
    NO_NODE_MARK = 'OC_Sol'
    ans = ''

    def pre_order(_root):
        nonlocal ans
        if not _root:
            ans += NO_NODE_MARK + ','
            return

        ans += _root.val + ','
        pre_order(_root.left)
        pre_order(_root.right)

    pre_order(root)  # O(n)
    return ans[:-1]


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree_pre_order(root):
    ans = ''

    def pre_order(_root):
        nonlocal ans
        if not _root:
            return

        ans += _root.val + ', '
        pre_order(_root.left)
        pre_order(_root.right)

    pre_order(root)  # O(n)
    print('Pre-Order binary tree:', ans[:-2])


node = Node('root', Node('left', Node('left.left')), Node('right'))
# print_tree_pre_order(node)
# print_tree_pre_order(deserialize(serialize(node)))
assert deserialize(serialize(node)).left.left.val == 'left.left'
