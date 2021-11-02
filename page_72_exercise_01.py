"""
Author: Ngo Van Chien
Date: 18/09/2021

Problem:   Assume that the variable amount refers to 24.325. Write the outputs of the following
statements:
a. print("Your salary is $%0.2f" % amount)
b. print("The area is %0.1f" % amount)
c. print("%7f" % amount)

Solution:

    ....
"""
soluong = 24.325
print ("Lương là $ " +  ("%0.2f" %soluong))
print ("Diện tích là " + ("%0.1f" %soluong))
print("%7f" % soluong)
