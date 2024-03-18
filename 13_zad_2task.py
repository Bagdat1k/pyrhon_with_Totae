a = input("1 - soz engiz")
b = input("2 - soz engiz")
a = a.lower()
b = b.lower()
if sorted(a) == sorted(b):
    print("this text anagramma")
else:
    print("this text not anagramma")