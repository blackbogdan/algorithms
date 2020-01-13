
Find Closest Value In BST
You are given a BST data structure consisting of BST nodes. You are also given a target integer value.
Each BST node has an integer value stored in a property called "value" and two children nodes stored in properties called "left" and "right" respectively.
A node is said to be a BST node if and only if it satisfies the BST properties:
1) its value is strictly greater than the values of every node to its left;
2) its value is less than or equal to the values of every node to its right;
3) both of its children nodes are either BST nodes themselves or None (null) values.



Write a function that finds the closest value to that target value contained in the BST.
Assume that there will only be one closest value.​
Example of input:
       10
       / \
      /   \
     /     \
    5      15
   / \     / \
  2   5   3  22
 / \
1  14,
Target number =12

Expected output: 13

# Recursive solution.
# Average case:
# time O(log(n)); space O(log(n)).
# Worst (when goes only to one direction, (e.g. has left nodes only)):
#  O(n), (O(n)); Where n - number of nodes.
# Space in this case will be occupied in memory by call stack.
def find_closest(tree, target):
    # we set closest to float("inf")
    return find_closest_helper(tree, target, float("inf"))

def find_closest_helper(tree, target, closest):
    if tree is None:
        # we got to last leaf. This is base condidion.
        return closest
    if abs(target - closest) > abs(target - tree.value):
        # target - closest - how far is target from previous closest value?
        # target - tree.value - how far is current value is far from target?
        # if current value is closer than previous closest, then we need to
        # update closest.
        closest = tree.value
    if target < tree.value:
        # current node is larger than target, we need to visit left node
        # in order to find smaller value
        return find_closest_helper(tree.left, target, closest)
    elif target > tree.value:
        # current node is smaller than target, we need to visit right node
        # in order to find larger value
        return find_closest_helper(tree.right, target, closest)
    else:
        # current node is equal to target. Return it
        return closest

# Iterative solution:
# Average case:
# time O(log(n)); space O(1).
# Worst (when goes only to one direction, (e.g. has left nodes only)):
#  O(n), (1); Where n - number of nodes.
# No call stack. We only store current closest value
def find_closest(tree, target):
    # we set closest to float("inf")
    currentNode = tree
    closest = float('inf')
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
