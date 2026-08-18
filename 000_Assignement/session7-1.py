
def remove_p(k):
    t = ""
    for i in k:
        if i.isalnum():
            t+=i
    return t.lower()

def str_feq(st):
    count = {}

    words = st.split(" ")

    for t in words:
        i = remove_p(t)
        if count.get(i) is None:
            count.update({i:1})
        else:
            d = count.get(i)
            d+=1
            count.update({i:d})
    return count

t = str_feq("hello, python Hello java")
print(t)

