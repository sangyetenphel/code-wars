import math
def sqInRect(lng, wdth):
    if lng == wdth: # if it's already a square return None
        return None
    
    squares = []
    while lng != wdth:
        if lng > wdth:
            squares.append(wdth)
            lng -= wdth
        else:
            squares.append(lng)
            wdth -= lng
    squares.append(lng)
    return squares

##def sqInRect(lng, wdth):
##    if lng == wdth:
##        return None
##    if lng < wdth:
##        wdth, lng = lng, wdth
##    res = []
##    while lng != wdth:
##        res.append(wdth)
##        lng = lng - wdth
##        if lng < wdth:
##            wdth, lng = lng, wdth
##    res.append(wdth)
##    return res

print(sqInRect(20, 14))
print(sqInRect(5, 3))


