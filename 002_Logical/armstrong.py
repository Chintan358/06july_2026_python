number = 103
temp= number
sum = 0
while number !=0:
    rem = number%10
    sum+=(pow(rem,3))
    number = number//10
    
if sum==temp:
    print(f"{temp} is armstrong")
else:
    print(f"{temp} is not armstrong")
