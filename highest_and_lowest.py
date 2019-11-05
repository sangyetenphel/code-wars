##def high_and_low(numbers):
##    """
##    All numbers are valid Int32, no need to validate them.
##    There will always be at least one number in the input string.
##    Output string must be two numbers separated by a single space, and highest number is first.
##    """
##    numbers_list_digit = numbers.split(" ")
##    numbers_list_int = []
##    for num in numbers_list_digit:
##        numbers_list_int.append(int(num))
##    return str(max(numbers_list_int)) + " " + str(min(numbers_list_int))
##

def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
