def reverse_message(message):
    st = ""
    for i in range(len(message)-1,-1,-1):
        st+=message[i]
    return st

print(reverse_message("hello"))