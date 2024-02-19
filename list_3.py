a = [5,9,3,7,1,2,8]
min_a = min(a)
max_a = max(a)
min_index = a.index(min_a)
max_index = a.index(max_a)

asd = a[min_index]
a[min_index] = a[max_index]
a[max_index] = asd
print(a)
