# l = [10,20,30,40,50,60]

# # for i in l:
# #     print(i)

# k = iter(l)

# print(next(k))


# # FileNotFoundErrordddfd

# # dfdfd

# # fdfd
# print(next(k))



# def test():
#     yield "Hello"
#     yield "test"

# k = test()
# print(next(k))
# print(next(k))


def square(a):
    for i in range(1,a):
        yield i*i
    
k = square(5)
print(next(k))
print(next(k))
print(next(k))
print(next(k))

