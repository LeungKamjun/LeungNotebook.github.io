list1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
list2 = [a for b in list1 for a in b]
print(list2)
list2 = []
for a in list1:
    for b in a:
        list2.append(b)
print(list2)