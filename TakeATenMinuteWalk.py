##def isValidWalk(walk):
##    #determine if walk is valid
##    if len(walk) != 10:
##        return False
##
##    count = {'e':0, "w":0, "n": 0, "s": 0}
##    for ele in walk:
##        count[ele] += 1
##
##    return count['e'] == count['w'] and count['n'] == count['s']

def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

#print(isValidWalk(['n','s','e','w','e','w','w','s','n','e']))
print(isValidWalk(['n','s','s','w','w','w','w','s','n','w']))
