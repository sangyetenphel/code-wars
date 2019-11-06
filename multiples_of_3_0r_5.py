##def solution(number):
##    multiples = []
##    for i in range(number):
##        if i % 3 == 0 or i % 5 == 0:
##            if i not in multiples:
##                multiples.append(i)
##
##    return sum(multiples)


def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
  
print(solution(0))
print(solution(1))
print(solution(10))
print(solution(25))
