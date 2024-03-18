def strings(words):
    split_w = words.split()
    return(sorted(split_w,key=len))
words = input("write text")
print(strings(words))