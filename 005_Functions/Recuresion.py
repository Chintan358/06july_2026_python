
# def square(a):
#     print(a*a)
#     a+=1
#     if a<20:
#         square(a)
    
# square(1)

def factorial(n):
    print(n)
    # Base case: 0! or 1! is 1
    if n == 0 or n == 1:
        return 1
    # Recursive step
    else:
        return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Output: 120