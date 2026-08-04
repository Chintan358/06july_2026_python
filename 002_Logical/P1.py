
lines = 5
for i in range(lines):
    for j in range(lines-i):
        print(" ",end="")
    for k in range((i*2)+1):
        if k==0 or k==(i*2) or i==lines-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()