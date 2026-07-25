number = 1111101111
p = 0
sum =0
while number!=0:
    rem = number%10
    sum+=(pow(2,p)*rem)
    number=number//10
    p+=1
print(sum)