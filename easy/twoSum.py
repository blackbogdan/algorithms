'''
Two SUM:

Write a function that takes in a non-empty arr of distinct integers and an integer representing a target sum.
If any two numbers in the input arr sum up to the target sum, the function should return them in an arr, in sorted order.
If no two numbers sum up to the target sum, the function should return an empty arr.
Assume that there will be at most one pair of numbers summing up to the target sum.​
Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
Sample output: [-1, 11]
'''

# time O(n) , space O(n)
def two_sum(arr, target):
    already_seen = set()
    for i in arr:
        cur_match = target - i
        if cur_match in already_seen:
            return sorted([cur_match, i])
        else:
            already_seen.add(i)
    return []

def two_sum(arr, target):
    arr.sort()
    left_index = 0
    right_index = len(arr) - 1
    while left_index < right_index:
        cur_sum = arr[left_index] + arr[right_index]
        if cur_sum ==  target:
            return [arr[left_index], arr[right_index]]
        elif cur_sum > target:
            right_index -= 1
        elif cur_sum < target:
            left_index +=1
    return []
