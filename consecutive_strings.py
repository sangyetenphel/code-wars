##def longest_consec(strarr, k):
##    """
##    strarr: array of strings
##    k: integer
##    return: first longest string consisting of k consecutive strings taken in the array.
##    """
##    if len(strarr) == 0 or k > len(strarr) or k <= 0:
##        return ""
##
##    result_list = []
##
##    for i in range(len(strarr) - (k-1)):
##        result = ''
##        for j in range(k):
##            result += strarr[i]
##            i += 1
##        result_list.append(result)
##
##    longest = 0
##    for ele in result_list:
##        if len(ele) > longest:
##            longest = len(ele)
##
##    for ele in result_list:
##        if len(ele) == longest:
##            return ele


def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result
    

#print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2)) #=> "abigailtheta"
#print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)) #=> "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)) #=> "ixoyx3452zzzzzzzzzzzz"
