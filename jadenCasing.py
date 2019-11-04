##def toJadenCase(string):
##    words = string.split(" ")
##    new_string = []
##    for word in words:
##        new_string.append(word[0].capitalize() + word[1:])
##    return (" ").join(new_string)

def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())

print(toJadenCase("How can mirrors be real if our eyes aren't real"))
