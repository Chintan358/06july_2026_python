# lines = 5
# for i in range(lines-1):
#     for k in range(lines-i):
#             print(" ",end="")
#     for j in range(i+1):
#         if j==0 or j==i:
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
# for i in range(lines):
#     for k in range(1+i):
#             print(" ",end="")
#     for j in range(lines-i):
#         if j==0 or j==lines-(i+1):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()


lines = 15
space=lines-1
star=1
mid = lines//2
for i in range(lines):
    for k in range(space):
        print(" ",end="")
    for j in range(star):
        if j==0 or j==star-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
    if i<mid:
        space-=1
        star+=1
    else:
        space+=1
        star-=1
        
        
# *****
# *   *
# *   *
# *   *
# *****

# *
# *
# *
# *
# *****

