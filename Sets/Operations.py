# Union
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 | set2)        #method1
print(set1.union(set2))    #method2


# intersection
set1 = {1,2,3}
set2 = {3,4,5,6}
print(set1 & set2)                 # method 1
print(set1.intersection(set2))     # method 2


# Difference
set1 = {1,2,3,4}
set2 = {3,4,5}
print(set1 - set2)               # method 1
print(set2.difference(set1))     # method 2


# symmetric difference
set1 = {1,2,3,4}
set2 = {3,4,5}
print(set1 ^ set2)                        # method 1
print(set1.symmetric_difference(set2))    # method 2
