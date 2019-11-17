##def score(dice):
##    # your code here
##    count = {}
##    total = 0
##    for ele in dice:
##        if ele not in count:
##            count[ele] = 1
##        else:
##            count[ele] += 1
##
##        if count[ele] == 3:
##            if ele == 1:
##                total += 1000
##            else:
##                total += ele * 100
##
##            count.pop(ele)
##
##    for ele in count:
##        if ele == 1:
##            total += count[ele] * 100
##        elif ele == 5:
##            total += 50 * count[ele]
##
##    return total


def score(dice): 
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    counter[die-1] += 1
  
  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

  return sum 

print(score([5,1,3,4,1]))
print(score([1,1,1,3,1]))
