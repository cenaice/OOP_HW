"""
Author: Victer Phiathep
Object Oriented Programming, Fall 2022

Test module for Homework 3, Problem 1
"""


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
        return L[:1] + replace_element(L[1:], oldel, newel)


def negative_sum(L):
    """
    The function returns True if L contains a pair of integers
    whose sum is negative and False otherwise
    """
    print(L)
    # L[0] will be passed and changed through the recursive loop
    if len(L) == 2:
        if L[0] + L[1] < 0:
            return True
        else:
            return False
    else:
        if L[0] + L[1] < 0:
            return True
        else:
            return negative_sum(L[2:])


def count_pattern(astr):
    """
    This function returns the number of times the substring 
    "ou" appears in the string.
    """
    # Base Case
    if len(astr) == 0:
        return 0
    else:

        # Checks for each pair
        if astr[0:2] == 'ou':
            # Add to count if pair of 'ou' is found
            return count_pattern(astr[1:]) + 1
        else:
            # Continue recursively without adding
            return count_pattern(astr[1:])


# Call functions here
