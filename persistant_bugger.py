##def persistence(n):
##    str_n = str(n)
##    count = 0
##    while len(str_n) > 1:
##        mul = 1
##        for digit in str_n:
##            mul *= int(digit)
##        str_n = str(mul)
##        count += 1
##    return count

from functools import reduce
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
        

print(persistence(39)) # => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

print(persistence(999))# => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

print(persistence(4))  # => 0   # Because 4 is already a one-digit number.
