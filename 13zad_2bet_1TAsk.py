def asd(list1, list2):
    return(set(list1).intersection(list2))


list1 = [1, 2, 3, 4, 85, 75]
list2 = [2, 5, 85, 1]
print(asd(list1,list2))