st = "hello python hello java hello java"

d = {}

words = st.split(" ")
for i in words:
    if d.get(i) is None:
        d.update({i:1})
    else:
        k = d.get(i)
        k+=1
        d.update({i:k})
        
        
print(d)