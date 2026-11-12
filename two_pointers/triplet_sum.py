"""""
Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0 . 
The solution must not contain duplicate triplets 
(e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates). 
If no such triplets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [[-3, 1, 2], [-1, 0, 1]]
"""

def triplet_sum(arr, target) :
    i = 0; length = len(arr)
    ans = set()
    arr.sort()
    while i < (length - 2) :
        j = i; k = length -1
        while j < k:
            if (arr[i] + arr[j] + arr[k]) == target :
                ans.add(tuple((arr[i], arr[j], arr[k])))
                j+=1; k-=1
            elif (arr[i] + arr[j] + arr[k]) < target :
                j += 1
            else:
                k -= 1
        i += 1
    return list(ans)

print("Arr: [0, -1, 2, -3, 1] target: ans: ", triplet_sum([0, -1, 2, -3, 1], 0))   