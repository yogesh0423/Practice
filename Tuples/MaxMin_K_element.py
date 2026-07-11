tup = (5, 20, 3, 7, 6, 8)
K = 3

temp = sorted(tup)
Min = temp[:K]
Max = temp[-K:]

print(Min)
print(Max)