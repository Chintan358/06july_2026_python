# d = {
#     "name":"tops",
#     "email":"tops@gmail.com",
#     "age":25,
#     25 : "abc",
    # (10,20,30):"fdfdd"
    # {10,20,30}:"ffdfd"
    # [10,20,30]:"xyz"
    # {"a":"a"}:"fd"
    # "age":27
# }
# print(type(d))
# print(d)


countries  = {
    "India":"IN",
    "USA":"US",
    "Canada":"CN"
}

# print(countries['India'])
# print(countries.get("India1"))

# print(countries.keys())
# print(countries.values())
# print(countries.items())

# countries["India"]="abc"
# countries["India1"]="abc"
# countries.update({"abc":"xyz"})
# print(countries)

# countries.pop("India")
# countries.popitem()
# countries.clear()
# del countries['India']
# del countries
# print(countries)

# for i,j in countries.items():
#     print(i,j)

# person = {
#     "name":"Dipesh",
#     "email":"dispesh@gmail.com",
#     "address": {
#         "city":"surat",
#         "area":"dindoli"
#     },
#     "languages":["gujarati","hindi","english"]
# }

# print(person['address']['city'])
# print(person['languages'][1])


# k =  {
#     "a":10,
#     "b":20
# }

# k.setdefault("b",50)
# print(k)

# x = ('key1', 'key2', 'key3')
# y = (1,2,3)

# thisdict = dict.fromkeys(x, y)

# print(thisdict)


# a = ("a","b","c")
# b = (10,20,30)
# k = zip(a,b)
# print(list(k))


a = []
print(type(a))
b = ()
print(type(b))
c = {}
print(type(c))
d = set()
print(type(d))