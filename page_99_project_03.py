"""
Author: Ngo Van Chien
Date: 18/09/2021

Problem:   Modify the guessing-game program of Section 3.5 so that the user thinks of a
number that the computer must guess. The computer must make no more than
the minimum number of guesses, and it must prevent the user from cheating by
entering misleading hints. (Hint: Use the math.log function to compute the minimum number of guesses needed after
the lower and upper bounds are entered.

Solution:

    ....
"""
import random
smaller = int(input("Nhập số nhỏ: "))
larger = int(input("Nhập số lớn: "))
myNumber = random.randint(smaller, larger)
count = 0

while True:
    count += 1
    userNumber = int(input("Khách: "))
    if userNumber < myNumber:
        print("Quá nhỏ")
    elif userNumber > myNumber:
        print("Quá lớn")
    else:
        print("Bạn đã nhận ", count, "tries!")





