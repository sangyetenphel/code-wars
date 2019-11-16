##def find_nb(m):
##    count = 0
##    cube = 0
##    while True:
##        count += 1
##        cube += count ** 3
##        if cube >= m:
##            break
##
##    if cube == m:
##        return count
##    else:
##        return -1

def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1

print(find_nb(1071225)) # 45
print(find_nb(91716553919377)) # -1
