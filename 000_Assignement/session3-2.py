scores = [56.7, 102.3, 88.9, 45.2, 120.8]

# k = map(lambda a:round(a),scores)
# print(list(k))

k = []
for i in scores:
    k.append(round(i))
    
print(k)