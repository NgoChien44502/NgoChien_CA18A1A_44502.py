"""
Author: Ngô Văn Chiến
Date: 17/10/2021
Problem: How would a column-major traversal of a grid work? Write a code segment that
prints the positions visited by a column-major traversal of a 2-by-3 grid.

Solution:
A nested loop is used traverse every position of a 2-dimensionalgrid. In a colum-major traversal,each row element
comprised in acolumn is visited before moving to the next column. The outer loopof the loop moves left to right across the column using thex-coordinate, and the inner loop moves down the row using thex-coordinate.


def grid_pos(x):
#number of rows
m=len(x)
#number of column
n=len(x[0])
    ....
"""