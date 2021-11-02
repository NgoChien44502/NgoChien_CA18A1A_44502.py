"""
Author: Ngô Văn Chiến
Date: 24/10/2021

Problem:
 A list is sorted in ascending order if it is empty or each item except the last one is
less than or equal to its successor. Define a predicate isSorted that expects a list
as an argument and returns True if the list is sorted, or returns False otherwise.
Solution:
    ....
"""
def isSorted(lyst):

    if len(lyst) == 0 or len(lyst) == 1:
        return True
    else:
        for index in range(len(lyst) - 1):
            if lyst[index] > lyst[index + 1]:
                return False
        return True


def main():
    lyst = []
    print(isSorted(lyst))
    lyst = [1]
    print(isSorted(lyst))
    lyst = list(range(10))
    print(isSorted(lyst))
    lyst[9] = 3
    print(isSorted(lyst))