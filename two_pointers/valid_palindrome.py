"""
A palindrome is a sequence of characters that reads the same forward and backward.

Given a string, determine if it's a palindrome after removing all non-alphanumeric characters. 
A character is alphanumeric if it's either a letter or a number.

Example 1:
Input: s = 'a dog! a panic in a pagoda.'
Output: True
Example 2:
Input: s = 'abc123'
Output: False
Constraints:
The string may include a combination of lowercase English letters, numbers, spaces, and punctuations.
"""


def is_palidrome(str) :
    start = 0; end = len(str) - 1

    while (start < end) :
        if not str[start].isalnum() :
            start+=1
            continue
        if not str[end].isalnum() :
            end-=1
            continue
        if str[start] != str[end]:
            return False
        start+=1
        end -= 1
    
    return True
        


print("Str: abc123 is_palindrome: ", is_palidrome("abc123"))
print("Str: a dog! a panic in a pagoda. is_palindrome: ", is_palidrome("a dog! a panic in a pagoda."))