# *****
#  ****
#   ***
#    **
#     *

lines = 5
for i in range(lines):
    for j in range(i):
        print(" ",end="")
    for k in range(lines-i):
        if k==0 or k==lines-i-1 or i==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()