"""Given an array of integers sorted in ascending order and a target value, 
return the indexes of any pair of numbers in the array that sum to the target. The order of the indexes in the result doesn't matter. 
If no pair is found, return an empty array."""

def pair_sum(arr, target) :
    i = 0 
    j = len(arr) -1
    ans = []
    while i < j :
        if (arr[i]+ arr[j]) == target :
            ans.extend([i, j])
            return ans
        elif (arr[i] + arr[j]) < target :
            i += 1
        else :
            j -= 1
    return ans

print(pair_sum([1, 2, 3, 4, 5, 6], 10))
print(pair_sum([1, 2, 3, 4, 5, 6], 2))

print("arr: [-5, -2, 3, 4, 6] target: 7 ans: ", pair_sum([-5, -2, 3, 4, 6], 7))
print("arr: [1, 1, 1] target: 7 ans: ", pair_sum([1, 1, 1], 2))