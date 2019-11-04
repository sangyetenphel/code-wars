##def isSquare(n):
##    if n == -1:
##        return False
##    return (n**0.5).is_integer()

import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;

print(isSquare(-1))
print(isSquare(0))
print(isSquare(3))
print(isSquare(4))
print(isSquare(25))
print(isSquare(26))
