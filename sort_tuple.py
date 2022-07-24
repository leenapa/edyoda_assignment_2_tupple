tuple1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list2 =[]
list3 =[]
for t in tuple1:
    list2.append(t[1],)
list2.sort()
for l in list2:
    for q in tuple1:
        if l == int(q[1],):
            list3.append(q)
print(list3)