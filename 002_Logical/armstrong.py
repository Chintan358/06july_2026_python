# for i in range(100,1000):
#     number = i
#     temp = number
#     sum = 0
#     while number!=0:
#         rem = number%10
#         sum+=(pow(rem,3))
#         number = number//10
        
#     if temp==sum:
#         print(f"{temp} is armstrong")
#     else:
#        # print(f"{temp} is not armstrong")
#        pass



number = int(input("Enter number : "))
l = len(str(number))
temp = number
sum = 0
while number!=0:
        rem = number%10
        sum+=(pow(rem,l))
        number = number//10
        
if temp==sum:
        print(f"{temp} is armstrong")
else:
       print(f"{temp} is not armstrong")
       