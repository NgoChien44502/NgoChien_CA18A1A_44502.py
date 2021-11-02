"""
Author: Ngo Van Chien
Date: 25/09/2021

Problem: Translate each of the following numbers to binary numbers:
a. 4710
b. 12710
c. 6410

Solution:
    ....
"""
print('Nhập số tp:')
tp = int(input())
st = []
while (tp!=0):
    sd = tp%2
    st.append(sd)
    tp=tp//2
print(st)
b=''
while (st!=[]):
    b=b+str(st.pop())
    print('Số nhị phân là',b)