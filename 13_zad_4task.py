def strings(string):
    uppercase_strings = []
    for s in string:
        if s.isupper():
            uppercase_strings.append(s)
    return uppercase_strings

string = ["BAga", "Bagdat","BAGA"]
print(strings(string))


