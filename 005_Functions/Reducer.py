l = [4,5,6,9,25,45,144,169,36,11,17,27]

from functools import reduce

# k  =reduce(lambda x,y : x if x>y else y ,l)
# print(k)
    
k = reduce(lambda x,y:x+y,l)
print(k)