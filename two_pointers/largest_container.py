"""
You are given an array of numbers, each representing the height of a vertical line on a graph. 
A container can be formed with any pair of these lines, along with the x-axis of the graph. 
Return the amount of water which the largest container can hold.

Input: heights = [2, 7, 8, 3, 7, 6]
Output: 24
"""

from math import inf


def largest_container(arr) :
    start = 0; end = len(arr) - 1
    ans = 0
    while start < end :
        ans = max(ans, (end - start) * min(arr[start], arr[end]))
        if arr[start] < arr[end]:
            start += 1
        else :
            end -= 1
    return ans

print("Input: [2, 7, 8, 3, 7, 6], largest capacity: ", largest_container([2, 7, 8, 3, 7, 6]))
