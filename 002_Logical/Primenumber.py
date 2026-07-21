total =0
for k in range(3,100):
    number = k
    flag = 0
    for i in range(2,number):
        if number%i==0:
            flag=1
            break
        
    if flag==0:
        total+=number
        print(f"{number} is Prime")
    else:
        # print(f"{number} is Not prime")
        pass
print(total)