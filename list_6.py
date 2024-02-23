a = [-2, 4, -5, -7, 3, 9, 10]

for i in range(len(a) - 1):
    if a[i] * a[i + 1] > 0:
        print(a[i], a[i + 1])
