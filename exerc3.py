
conj1 = set([0,1,3,6,9,12])
conj2 = set([0,2,4,6,8,10,12])


print(len(conj1) + len(conj2) - len(conj1.intersection(conj2)))
print(conj1.intersection(conj2))
print(conj1.union(conj2))
print(conj1.difference(conj2))
print(conj2.difference(conj1))

