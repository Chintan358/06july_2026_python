# l = [1,2,3,4,5,5,"abc",45.66,True]
# print(l)
# print(type(l))
# print(len(l))

# k = list((10,20,30,40))
# print(k)


subjects = ["python","java","php","android","node"]
# print(subjects[0])
# print(subjects[-1])
# print(subjects[2:4])
# print(subjects[::-1])

# subjects[0] = "abc"
# subjects[2:4] = ["abc","xyz","pqr"]
# subjects.insert(1,"abc")
# subjects.append("abc")
# subjects.extend(['1','2',3])


# subjects.remove("python")
# subjects.pop(1)
# subjects.clear()
# del subjects
# print(subjects)


# for i in subjects:
#     print(i)

# for i in range(len(subjects)):
#     print(subjects[i])

# i=0
# while i<len(subjects):
#     print(subjects[i])
#     i+=1

k = [1,20,8,40,55,6,7,8]

# d = []
# for i in k:
#     d.append(i*i)
# print(d)

# d = [i*i for i in k]
# d = [i for i in k]
# print(d)

# k.sort()
# k.sort(reverse=1)
# k.reverse()
# print(k)

# l = sorted(k)
# print(l)

# a = [10,20,30]
# b = a
# # b = list(a)
# b.append(1000)

# print(a)
# print(b)

# a = [10,20,30,40,40]
# print(a.count(10))
# print(a.index(10))

k = [10,20,30,40]

j = [x for x in k if x==30]
print(j)