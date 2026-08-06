l = [1,5,9,8,7,6,4,6,2,35,74]

# def check_odd(a):
#     if a%2!=0:
#         return a
    
# r = []
# for i in l:
#     k = check_odd(i)
#     if k is not None:
#         r.append(k)
# print(r)

# r = filter(check_odd,l)
# r = filter(lambda k : k%2!=0,l)
# print(list(r))

# sub = ["python","java","php","android","node"]

# k = filter(lambda r:r.startswith("p"),sub)
# k = filter(lambda r:'a' in r,sub)
# print(list(k))

import math

l = [4,5,6,9,25,45,144,169,36,11,17,27]
k = filter(lambda x :math.sqrt(x).is_integer(),l)
print(list(k))
