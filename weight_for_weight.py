##def order_weight(strng):
##    nl = []
##    l = strng.split(" ")
##    for digits in l:
##        sum = 0
##        for digit in digits:
##            sum += int(digit)
##        nl.append([digits, sum])
##
##    fl = sorted(nl, key = lambda x: x[1])
##    #print(fl)
##
##    for i in range(len(fl)):
##        j = i + 1
##        while j < len(fl) and fl[i][1] == fl[j][1]:
##            if fl[i][0] > fl[j][0]:
##                #print(fl[i][0], fl[i+1][0])
##                fl[i], fl[j] = fl[j], fl[i]
##                j += 1
##            else:
##                j += 1
##
##    #print(fl)
##
##    result = ''
##    for ele in fl:
##        result += ele[0] + " "
##
##    return result[:-1]

def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split(' ')), key=lambda x: sum(int(c) for c in x)))

#print(order_weight("103 123 4444 99 2000")) # "2000 103 123 4444 99"
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")) #"11 11 2000 10003 22 123 1234000 44444444 9999' 

