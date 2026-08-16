# subset
set1 = {1,2,3,4,5}
set2 = {1,2,3}
print(set2.issubset(set1))
print(set1 <= set2)


# superset
set1 = {10,20,30,40}
set2 = {20,30}
print(set1.issuperset(set2))


#disjoint()
set1 = {1,2,3}
set2 = {1,5,6}
print(set1.isdisjoint(set2))


# frozen set
numbers = frozenset({10,20,30,40})
print(numbers)
