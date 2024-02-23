a = [3, 7, 2 ,9, 1, 5, 8, 4]

for i in range(1 ,len(a)):
    if a[i] > a[i - 1]:
        print(a[i])
