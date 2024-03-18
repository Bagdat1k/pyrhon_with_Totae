def word(text):
    return(set('abcdefghijklmnopqrstuvwxyz') == set(text.lower().replace(" ","")))

text = input("pishi text")
print(word(text))