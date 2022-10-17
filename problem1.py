"""
Author: Victer Phiathep
Object Oriented Programming, Fall 2022

Test module for Homework 3, Problem 1
"""


from itertools import count


def replace_element(L, oldel, newel):
    """
    This function returns a list in which every occurence of 
    oldel in L has been replaced with newel.
    """
    if L == []:
        return L
    else:
        if L[0] == oldel:
            L[0] = newel
        # Can add sliced operands together
        return L[:1] + replace_element(L[1:], oldel, newel)

def negative_sum(L):
    """
    The function returns True if L contains a pair of integers
    whose sum is negative and False otherwise
    """
    if L == []:
        return 0
    else:
        return L[0] + negative_sum(L[1:]) 
    

def count_pattern(astr):
    """
    This function returns the number of times the substring 
    "ou" appears in the string.
    """
    if len(astr) == 2:
        return count
    else:
        if astr[:2] == 'ou':
            count += 1
        return count + astr[1:]


    

# L = [5, 4, 3, 5, 1]
# print(L[1:] + L[1:3])
# print(replace_element(L, 5, 100))

# arr = [12, 8, 10, -50] 
# print(negative_sum(arr))


count_pattern('ouse mouse louse')