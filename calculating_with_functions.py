##def zero(*args):
##    if args:
##        operator = args[0][0]
##        operand = args[0][1]
##        if operator == "add":
##            return 0 + operand
##        elif operator == "sub":
##            return 0 - operand
##        elif operator == "mul":
##            return 0 * operand
##        elif operator == "div":
##            return 0 // operand
##    else:
##        return 0
##    
##def one(*args): 
##    if args:
##        operator = args[0][0]
##        operand = args[0][1]
##        if operator == "add":
##            return 1 + operand
##        elif operator == "sub":
##            return 1 - operand
##        elif operator == "mul":
##            return 1 * operand
##        elif operator == "div":
##            return 1 // operand
##    else:
##        return 1
##
##def two(*args): 
##    if args:
##        operator = args[0][0]
##        operand = args[0][1]
##        if operator == "add":
##            return 2 + operand
##        elif operator == "sub":
##            return 2 - operand
##        elif operator == "mul":
##            return 2 * operand
##        elif operator == "div":
##            return 2 // operand
##    else:
##        return 2
##    
##def three(*args):
##    if args:
##        operator = args[0][0]
##        operand = args[0][1]
##        if operator == "add":
##            return 3 + operand
##        elif operator == "sub":
##            return 3 - operand
##        elif operator == "mul":
##            return 3 * operand
##        elif operator == "div":
##            return 3 // operand
##    else:
##        return 3
##
##def four(*args):
##    if args:
##        operator = args[0][0]
##        operand = args[0][1]
##        if operator == "add":
##            return 4 + operand
##        elif operator == "sub":
##            return 4 - operand
##        elif operator == "mul":
##            return 4 * operand
##        elif operator == "div":
##            return 4 // operand
##    else:
##        return 4
##    
##def five(*args):
##    if args:
##        operator = args[0][0]
##        operand = args[0][1]
##        if operator == "add":
##            return 5 + operand
##        elif operator == "sub":
##            return 5 - operand
##        elif operator == "mul":
##            return 5 * operand
##        elif operator == "div":
##            return 5 // operand
##    else:
##        return 5
##    
##def six(*args):
##    if args:
##        operator = args[0][0]
##        operand = args[0][1]
##        if operator == "add":
##            return 6 + operand
##        elif operator == "sub":
##            return 6 - operand
##        elif operator == "mul":
##            return 6 * operand
##        elif operator == "div":
##            return 6 // operand
##    else:
##        return 6
##    
##def seven(*args):
##    if args:
##        operator = args[0][0]
##        operand = args[0][1]
##        if operator == "add":
##            return 7 + operand
##        elif operator == "sub":
##            return 7 - operand
##        elif operator == "mul":
##            return 7 * operand
##        elif operator == "div":
##            return 7 // operand
##    else:
##        return 7
##    
##def eight(*args):
##    if args:
##        operator = args[0][0]
##        operand = args[0][1]
##        if operator == "add":
##            return 8 + operand
##        elif operator == "sub":
##            return 8 - operand
##        elif operator == "mul":
##            return 8 * operand
##        elif operator == "div":
##            return 8 // operand
##    else:
##        return 8
##    
##def nine(*args):
##    if args:
##        operator = args[0][0]
##        operand = args[0][1]
##        if operator == "add":
##            return 9 + operand
##        elif operator == "sub":
##            return 9 - operand
##        elif operator == "mul":
##            return 9 * operand
##        elif operator == "div":
##            return 9 // operand
##    else:
##        return 9
##    
##
##def plus(operand): 
##    return "add", operand
##
##def minus(operand): 
##    return "sub", operand
##
##def times(operand):
##    return "mul", operand
##
##def divided_by(operand):
##    return "div", operand


def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y


print(zero(divided_by(one())))
