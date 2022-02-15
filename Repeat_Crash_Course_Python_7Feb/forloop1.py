for x in range(5):
    print(x)

#range of num will start from 0 by default#
#List of num generated will be 1 less than the value#

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum  