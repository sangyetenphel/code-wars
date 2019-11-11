import math
import time

def is_prime(num): # The fastest way to check for a prime
    if num <= 1:
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:  # cause we are later skipping all even numbers as it not prime i.e divisble by 2
        return False

    max_div = math.floor(math.sqrt(num))
    for i in range(3, max_div + 1, 2):  #  looping only till the square root of that number and only the odd numbers 
        if num % i == 0:
            return False

    return True   # Time required: 0.26

##def is_prime(num):  # is faster as we only loop through halfway through num
##    if num <= 1:
##        return False
##
##    
##    max_div = math.floor(math.sqrt(num)) # get the square root of the num 
##    for i in range(2, max_div + 1): # only loop till the square root of that num i.e. O(logn)
##        if num % i == 0:
##            return False
##
##    return True    # Time Required: 0.33
    
##def is_prime(num):   # is slow since we loop all the way to num O(n)
##    if num <= 1:
##        return False
##    i = 2
##    while i < num:
##        if num % i == 0:
##            return False
##        i += 1
##
##    return True      # Time Required: 74.26


##def is_prime(num):
##    return num > 1 and not any(num % n == 0 for n in range(2,num))


# Driver function
t0 = time.time()
c = 0 # for counting

for n in range(1,100000):
    x = is_prime(n)
    c += x
print("Toral prime numbers in range :", c)

t1 = time.time()
print("Time required :", t1 - t0)

print(is_prime(-5))
print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(5))
print(is_prime(8))


