##def find_next_square(sq):
##    # Return the next square if sq is a square, -1 otherwise
##    i = 0
##    while i <= sq:
##        if i*i == sq:
##            return (i+1) * (i+1)
##        elif i * i > sq:
##            return -1
##        i += 1
##    return -1

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

print(find_next_square(121))
print(find_next_square(0))
print(find_next_square(1))
print(find_next_square(625))
print(find_next_square(114))
