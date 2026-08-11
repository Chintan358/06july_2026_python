# f = open("D://test.txt","w")
# f.write("hello python")
# f.close()

# f = open("test.txt")
# data = f.read()
# print(data)

# f = open("test.txt","a")
# f.write("hello python")
# f.close()


# f = open("test.txt","w")
# # f.write("hello python")
# l = ["hello python \n","hello java \n","helo tops"]
# f.writelines(l)
# f.close()


# f = open("test.txt","r")
# data = f.read()
# print(data)

# while True: 
#     data = f.readline()
#     if not data:
#         break
#     print(len(data))

# # data = f.readlines()
# # print(data)
# f.close()

# with open("test.txt",'r') as f :
#     data = f.read()
#     print(data)

# with open("test.txt",'r') as f :
#     f.seek(10)
#     print(f.tell())
#     data = f.read()
#     print(f.tell())
#     print(data)





# with open("home.txt",'r+') as f:
#     f.write("write something")
#     f.seek(0)
#     data =f.read()
#     print(data)

# with open("cat.jpg",'rb') as f:
#     data = f.read()
#     print(data)

import json
d = {"name":"manthan","email":"manthon@gmail.com"}
# with open("data.json","w") as f:
#     json.dump(d,f)

with open("data.json","r") as f:
    data = json.load(f)
    print(data)